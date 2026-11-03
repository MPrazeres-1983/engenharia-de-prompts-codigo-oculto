import argparse
import json
from .core import exportar_contexto, responder


def main():
    parser = argparse.ArgumentParser(description="Lavandaria fictícia: pesquisa e templates offline; sem LLM.")
    parser.add_argument("--cliente", choices=["cliente-A", "cliente-B"], required=True,
                        help="Escolhe um papel de demonstração; não autentica um utilizador.")
    parser.add_argument("--pergunta", required=True)
    parser.add_argument("--exportar-contexto", action="store_true")
    args = parser.parse_args()
    try:
        resultado = exportar_contexto(args.pergunta, args.cliente) if args.exportar_contexto else responder(args.pergunta, args.cliente)
    except (ValueError, PermissionError) as exc:
        parser.exit(2, str(exc) + "\n")
    print(json.dumps(resultado, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
