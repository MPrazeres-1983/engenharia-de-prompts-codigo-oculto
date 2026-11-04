"""Verifica estrutura editorial, referências, laboratórios, JSON e log de LaTeX.

Não é um parser LaTeX completo nem certifica correção científica. Só usa stdlib.
"""
import argparse
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]


def verificar(log=None):
    erros = []
    entrada = ROOT / "src/livro.tex"
    principal = entrada.read_text(encoding="utf-8")
    ficheiros = [entrada]
    for relativo in re.findall(r"\\input\{([^}]+)\}", principal):
        p = ROOT / "src" / (relativo + ".tex")
        if not p.is_file():
            erros.append(f"Input inexistente: {relativo}")
        else:
            ficheiros.append(p)
    textos = [p.read_text(encoding="utf-8") for p in ficheiros]
    fonte = "\n".join(textos)
    labels = re.findall(r"\\label\{([^}]+)\}", fonte)
    duplicados = sorted({label for label in labels if labels.count(label) > 1})
    erros += [f"Label duplicada: {label}" for label in duplicados]
    refs = re.findall(r"\\(?:c|C|page)?ref\{([^}]+)\}", fonte)
    erros += [f"Referência sem label: {ref}" for ref in refs if ref not in labels]
    bib = (ROOT / "src/referencias.bib").read_text(encoding="utf-8")
    chaves = re.findall(r"@\w+\{([^,]+),", bib)
    erros += [f"Chave BibTeX duplicada: {k}" for k in set(chaves) if chaves.count(k) > 1]
    citadas = [k.strip() for grupo in re.findall(r"\\cite\w*\{([^}]+)\}", fonte) for k in grupo.split(",")]
    erros += [f"Citação sem entrada: {k}" for k in sorted(set(citadas)-set(chaves))]
    laboratorios = 0
    jsons = 0
    for p, texto in zip(ficheiros, textos):
        for corpo in re.findall(r"\\begin\{promptlabbox\}\{[^\n]+\}\n(.*?)\\end\{promptlabbox\}", texto, re.S):
            laboratorios += 1
            for termo in ["Objetivo e contexto:", "Resultado", "Valida", "Falhas possíveis:"]:
                if termo.casefold() not in corpo.casefold():
                    erros.append(f"Laboratório sem {termo}: {p.name}")
        for bloco in re.findall(r"\\begin\{lstlisting\}(.*?)\\end\{lstlisting\}", texto, re.S):
            if bloco.strip().startswith("{"):
                candidato = bloco.strip()
                try:
                    # Alguns prompts incluem uma instância JSON seguida das instruções.
                    _, fim = json.JSONDecoder().raw_decode(candidato)
                    jsons += 1
                except json.JSONDecodeError as exc:
                    erros.append(f"Instância JSON inválida em {p.name}: {exc}")
    capitulos = len(re.findall(r"\\input\{capitulos/[0-9]", principal))
    manifesto = json.loads((ROOT / "docs/V3_ESTRUTURA.json").read_text(encoding="utf-8"))
    esperados = [f for parte in manifesto['partes'] for f in parte['capitulos']]
    encontrados = re.findall(r"\\input\{(capitulos/[0-9][^}]+)\}", principal)
    if encontrados != esperados:
        erros.append("Capítulos ou ordem diferentes do manifesto V3")
    if len(set(esperados)) != len(esperados):
        erros.append("Capítulo repetido no manifesto V3")
    if re.findall(r"\\part\{([^}]+)\}", principal) != [p['titulo'] for p in manifesto['partes']]:
        erros.append("Partes ou ordem diferentes do manifesto V3")
    apendices = re.findall(r"\\input\{(capitulos/ap-[^}]+)\}", principal)
    if apendices != manifesto['apendices']:
        erros.append("Apêndices diferentes do manifesto V3")
    if laboratorios != manifesto['laboratorios_esperados']:
        erros.append(f"Esperados {manifesto['laboratorios_esperados']} laboratórios: {laboratorios}")
    for p in sorted((ROOT / "exemplos").rglob("*.json")):
        try:
            json.loads(p.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError) as exc:
            erros.append(f"Ficheiro JSON inválido: {p.name}: {exc}")
    if log is not None:
        path = Path(log)
        if not path.is_absolute(): path = ROOT / path
        if not path.is_file():
            erros.append(f"Log inexistente: {path}")
        else:
            conteudo = path.read_text(encoding="utf-8", errors="replace")
            padroes = [r"Overfull \\[hv]box", r"Citation .+ undefined", r"Reference .+ undefined",
                       r"There were undefined", r"Missing character", r"LaTeX Error", r"Package .+ Error",
                       r"Rerun to get", r"Rerun to get citations", r"Negative labelwidth"]
            for padrao in padroes:
                if re.search(padrao, conteudo): erros.append(f"Aviso/erro no log: {padrao}")
    resultado = {"capitulos": capitulos, "laboratorios": laboratorios,
                 "referencias_bibliograficas": len(chaves), "instancias_json": jsons,
                 "erros": erros, "nota": "Validação estática; não certifica conteúdo científico ou legibilidade visual."}
    return resultado


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--log")
    args = parser.parse_args()
    resultado = verificar(args.log)
    print(json.dumps(resultado, ensure_ascii=False, indent=2))
    sys.exit(bool(resultado["erros"]))
