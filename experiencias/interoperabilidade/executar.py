"""Ensaio local da Lavandaria. HTTP no loopback e JSON-RPC num subprocesso."""

import argparse
from http.client import HTTPConnection
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import re
import subprocess
import sys
from threading import Thread
from uuid import uuid4

from exemplos.lavandaria.core import executar_ferramenta


MCP = "2026-07-28"
A2A = "1.0"
PREFIXO = "io.modelcontextprotocol/"
FERRAMENTA = "consultar_estado"
CREDENCIAIS = {"Bearer ensaio-A": "cliente-A", "Bearer ensaio-B": "cliente-B"}
AGUARDA = "TASK_STATE_INPUT_REQUIRED"
CONCLUIDA = "TASK_STATE_COMPLETED"
FALHOU = "TASK_STATE_FAILED"


def resposta_mcp(pedido, cliente):
    resposta = {"jsonrpc": "2.0", "id": pedido.get("id")}
    parametros = pedido.get("params")
    if pedido.get("jsonrpc") != "2.0" or type(parametros) is not dict:
        return {**resposta, "error": {"code": -32600, "message": "Pedido inválido"}}
    meta = parametros.get("_meta")
    if type(meta) is not dict or type(meta.get(PREFIXO + "clientCapabilities")) is not dict:
        return {**resposta, "error": {"code": -32602, "message": "Metadados em falta"}}
    versao = meta.get(PREFIXO + "protocolVersion")
    if versao != MCP:
        return {**resposta, "error": {"code": -32022, "message": "Versão MCP não suportada",
                                      "data": {"requested": versao, "supported": [MCP]}}}
    resultado = {"resultType": "complete", "_meta": {
        PREFIXO + "serverInfo": {"name": "arquivo-lavandaria", "version": "1.0.0"},
    }}
    metodo = pedido.get("method")
    if metodo == "server/discover":
        resultado.update(supportedVersions=[MCP], capabilities={"tools": {}})
    elif metodo == "tools/list":
        resultado["tools"] = [{
            "name": FERRAMENTA, "description": "Consulta o estado de uma reclamação fictícia.",
            "inputSchema": {"type": "object", "required": ["reclamacao_id"],
                            "properties": {"reclamacao_id": {"type": "string", "pattern": "^LAV-[0-9]{3}$"}},
                            "additionalProperties": False},
        }]
    elif metodo == "tools/call":
        try:
            documento = executar_ferramenta(parametros.get("name"), parametros.get("arguments"),
                                             cliente_autenticado=cliente)
            texto, erro = documento.texto, False
        except PermissionError as exc:
            texto, erro = str(exc), True
        except ValueError:
            return {**resposta, "error": {"code": -32602, "message": "Ferramenta ou argumentos inválidos"}}
        resultado.update(content=[{"type": "text", "text": texto}], isError=erro)
    else:
        return {**resposta, "error": {"code": -32601, "message": "Método indisponível neste ensaio"}}
    return {**resposta, "result": resultado}


def chamar_mcp(cliente, metodo, argumentos=None, versao=MCP):
    pedido = {"jsonrpc": "2.0", "id": 1, "method": metodo, "params": {
        "_meta": {PREFIXO + "protocolVersion": versao, PREFIXO + "clientCapabilities": {},
                  PREFIXO + "clientInfo": {"name": "rececao-lavandaria", "version": "1.0.0"}},
        **(argumentos or {}),
    }}
    processo = subprocess.run(
        [sys.executable, "-m", "experiencias.interoperabilidade.executar", "--arquivo", cliente],
        input=json.dumps(pedido) + "\n", capture_output=True, encoding="utf-8", timeout=5, check=True,
    )
    resposta = json.loads(processo.stdout)
    if resposta.get("jsonrpc") != "2.0" or resposta.get("id") != pedido["id"]:
        raise ValueError("A resposta MCP não corresponde ao pedido")
    return resposta


def cartao(porta):
    return {
        "name": "Receção da Lavandaria", "description": "Consulta didática de reclamações.",
        "version": "1.0.0", "supportedInterfaces": [{
            "url": f"http://127.0.0.1:{porta}", "protocolBinding": "HTTP+JSON", "protocolVersion": A2A,
        }],
        "capabilities": {}, "defaultInputModes": ["text/plain"], "defaultOutputModes": ["text/plain"],
        "skills": [{"id": FERRAMENTA, "name": "Consultar estado", "description": "Leitura autorizada.",
                    "tags": ["lavandaria", "consulta"]}],
        "securitySchemes": {"ensaio": {"httpAuthSecurityScheme": {"scheme": "bearer"}}},
        "securityRequirements": [{"schemes": {"ensaio": {"list": []}}}],
    }


class Rececao(BaseHTTPRequestHandler):
    """Apenas as operações do ensaio, com tarefas em memória e servidor sequencial."""

    def setup(self):
        super().setup()
        self.connection.settimeout(5)

    def log_message(self, formato, *args):
        pass

    def devolver(self, codigo, valor):
        corpo = json.dumps(valor, ensure_ascii=False).encode("utf-8")
        self.send_response(codigo)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(corpo)))
        if codigo == 401:
            self.send_header("WWW-Authenticate", "Bearer")
        self.end_headers()
        self.wfile.write(corpo)

    def erro(self, codigo, estado, texto, motivo=None, metadados=None):
        erro = {"code": codigo, "status": estado, "message": texto}
        if motivo:
            erro["details"] = [{"@type": "type.googleapis.com/google.rpc.ErrorInfo",
                                "domain": "a2a-protocol.org", "reason": motivo,
                                "metadata": metadados or {}}]
        self.devolver(codigo, {"error": erro})

    def cliente(self):
        identidade = CREDENCIAIS.get(self.headers.get("Authorization"))
        if identidade is None:
            self.erro(401, "UNAUTHENTICATED", "Credencial de ensaio em falta ou inválida")
            return None
        if self.headers.get("A2A-Version") != A2A:
            self.erro(400, "FAILED_PRECONDITION", "Versão A2A não suportada",
                      "VERSION_NOT_SUPPORTED", {"supportedVersions": A2A})
            return None
        return identidade

    def tarefa(self, identificador, cliente):
        registo = self.server.tarefas.get(identificador)
        if registo is None or registo[0] != cliente:
            self.erro(404, "NOT_FOUND", "Tarefa indisponível", "TASK_NOT_FOUND")
            return None
        return registo[1]

    def do_GET(self):
        if self.path == "/.well-known/agent-card.json":
            self.devolver(200, cartao(self.server.server_port))
            return
        cliente = self.cliente()
        if cliente is not None:
            tarefa = self.tarefa(self.path.removeprefix("/tasks/"), cliente)
            if tarefa is not None:
                self.devolver(200, tarefa)

    def ler_mensagem(self):
        tamanho = int(self.headers.get("Content-Length", "0"))
        if not 0 < tamanho <= 8192:
            raise ValueError("Tamanho inválido")
        mensagem = json.loads(self.rfile.read(tamanho))["message"]
        partes = mensagem["parts"]
        texto = partes[0]["text"]
        if (mensagem["role"] != "ROLE_USER" or len(partes) != 1 or not isinstance(texto, str)
                or not isinstance(mensagem["messageId"], str) or not mensagem["messageId"]):
            raise ValueError("Mensagem fora do caso de ensaio")
        if "taskId" in mensagem and not isinstance(mensagem["taskId"], str):
            raise ValueError("Identificador inválido")
        return mensagem, texto

    def do_POST(self):
        cliente = self.cliente()
        if cliente is None:
            return
        if self.path != "/message:send":
            self.erro(404, "NOT_FOUND", "Operação indisponível")
            return
        try:
            mensagem, texto = self.ler_mensagem()
        except (ValueError, KeyError, TypeError, IndexError):
            self.erro(400, "INVALID_ARGUMENT", "Esperada uma mensagem com uma parte de texto")
            return
        if "taskId" in mensagem:
            tarefa = self.tarefa(mensagem["taskId"], cliente)
            if tarefa is None:
                return
            if tarefa["status"]["state"] != AGUARDA:
                self.erro(400, "FAILED_PRECONDITION", "A tarefa já terminou", "UNSUPPORTED_OPERATION")
                return
            if mensagem.get("contextId", tarefa["contextId"]) != tarefa["contextId"]:
                self.erro(400, "INVALID_ARGUMENT", "Contexto diferente do da tarefa")
                return
        else:
            tarefa = {"id": str(uuid4()), "contextId": str(uuid4())}
        reclamacao = re.search(r"\bLAV-[0-9]{3}\b", texto.upper())
        if reclamacao is None:
            tarefa["status"] = estado(AGUARDA, "Indica o número da reclamação.", tarefa)
        else:
            try:
                resposta = chamar_mcp(cliente, "tools/call", {
                    "name": FERRAMENTA, "arguments": {"reclamacao_id": reclamacao.group()},
                })["result"]
                conteudo = resposta["content"][0]["text"]
                if resposta["isError"]:
                    tarefa["status"] = estado(FALHOU, conteudo, tarefa)
                else:
                    tarefa["status"] = {"state": CONCLUIDA}
                    tarefa["artifacts"] = [{"artifactId": str(uuid4()), "name": "Estado",
                                            "parts": [{"text": conteudo}]}]
            except (subprocess.SubprocessError, ValueError, KeyError, IndexError):
                tarefa["status"] = estado(FALHOU, "O arquivo não respondeu como esperado.", tarefa)
        self.server.tarefas[tarefa["id"]] = (cliente, tarefa)
        self.devolver(200, {"task": tarefa})


def estado(nome, texto, tarefa):
    return {"state": nome, "message": {"messageId": str(uuid4()), "role": "ROLE_AGENT",
                                       "taskId": tarefa["id"], "contextId": tarefa["contextId"],
                                       "parts": [{"text": texto}]}}


def pedir_http(porta, caminho, credencial="ensaio-A", corpo=None, versao=A2A):
    ligacao = HTTPConnection("127.0.0.1", porta, timeout=8)
    cabecalhos = {"A2A-Version": versao, "Content-Type": "application/json"}
    if credencial:
        cabecalhos["Authorization"] = f"Bearer {credencial}"
    try:
        ligacao.request("GET" if corpo is None else "POST", caminho,
                        body=None if corpo is None else json.dumps(corpo), headers=cabecalhos)
        resposta = ligacao.getresponse()
        return resposta.status, json.loads(resposta.read())
    finally:
        ligacao.close()


def enviar_mensagem(porta, texto, credencial="ensaio-A", tarefa=None):
    mensagem = {"messageId": str(uuid4()), "role": "ROLE_USER", "parts": [{"text": texto}]}
    if tarefa is not None:
        mensagem.update(taskId=tarefa["id"], contextId=tarefa["contextId"])
    return pedir_http(porta, "/message:send", credencial, {"message": mensagem})


def verificar(porta):
    resultados = []

    def conferir(condicao, nome, observado):
        if not condicao:
            raise AssertionError(f"{nome}: {observado}")
        resultados.append({"caso": nome, "observado": observado})

    descoberta = chamar_mcp("cliente-A", "server/discover")["result"]
    lista = chamar_mcp("cliente-A", "tools/list")["result"]["tools"]
    conferir(descoberta["supportedVersions"] == [MCP] and lista[0]["name"] == FERRAMENTA,
             "Descobrir ferramenta MCP", FERRAMENTA)
    antiga = chamar_mcp("cliente-A", "server/discover", versao="2025-11-25")["error"]
    conferir(antiga["code"] == -32022 and antiga["data"]["supported"] == [MCP],
             "Rejeitar versão MCP incompatível", antiga["code"])
    invalidos = chamar_mcp("cliente-A", "tools/call", {
        "name": FERRAMENTA, "arguments": {"reclamacao_id": "LAV-002", "cliente_id": "cliente-B"},
    })
    conferir(invalidos.get("error", {}).get("code") == -32602 and "result" not in invalidos,
             "Rejeitar identidade nos argumentos MCP", invalidos.get("error"))

    codigo, ficha = pedir_http(porta, "/.well-known/agent-card.json", credencial=None)
    interface = ficha["supportedInterfaces"][0]
    conferir(codigo == 200 and interface["protocolVersion"] == A2A
             and interface["protocolBinding"] == "HTTP+JSON" and ficha["skills"][0]["id"] == FERRAMENTA,
             "Descobrir serviço A2A", interface["protocolBinding"])
    codigo, pedido = enviar_mensagem(porta, "Qual é o estado da reclamação?")
    tarefa = pedido["task"]
    conferir(codigo == 200 and tarefa["status"]["state"] == AGUARDA and not tarefa.get("artifacts"),
             "Pedir o número em falta", tarefa["status"]["state"])
    caminho = "/tasks/" + tarefa["id"]
    bloqueado = pedir_http(porta, caminho, "ensaio-B")
    inexistente = pedir_http(porta, "/tasks/" + str(uuid4()), "ensaio-B")
    nova_tentativa = enviar_mensagem(porta, "LAV-002", "ensaio-B", tarefa)
    conferir(bloqueado == inexistente == nova_tentativa and bloqueado[0] == 404,
             "Isolar consulta e retoma de tarefas", bloqueado[0])
    conferir(pedir_http(porta, caminho) == (200, tarefa)
             and pedir_http(porta, caminho, credencial=None)[0] == 401,
             "Preservar tarefa e exigir credencial", "200 para A e 401 sem credencial")

    codigo, final = enviar_mensagem(porta, "É a LAV-001", tarefa=tarefa)
    concluida = final["task"]
    conteudo = concluida["artifacts"][0]["parts"][0]["text"]
    conferir(codigo == 200 and concluida["id"] == tarefa["id"]
             and concluida["status"]["state"] == CONCLUIDA and conteudo == "LAV-001: em análise."
             and pedir_http(porta, caminho) == (200, concluida),
             "Concluir a mesma tarefa com artefacto", conteudo)
    falhas = []
    for identificador in ("LAV-002", "LAV-999"):
        codigo, retorno = enviar_mensagem(porta, identificador)
        falha = retorno["task"]
        if codigo != 200 or falha["status"]["state"] != FALHOU or falha.get("artifacts"):
            raise AssertionError("Uma consulta recusada não pode produzir um artefacto")
        falhas.append(falha["status"]["message"]["parts"][0]["text"])
    conferir(falhas[0] == falhas[1], "Equiparar reclamação privada e ausente", falhas[0])
    codigo, propria = enviar_mensagem(porta, "LAV-002", "ensaio-B")
    texto = propria["task"]["artifacts"][0]["parts"][0]["text"]
    conferir(codigo == 200 and propria["task"]["status"]["state"] == CONCLUIDA
             and texto == "LAV-002: aguarda contacto.", "Consultar como o titular", texto)
    return resultados


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--arquivo", choices=tuple(CREDENCIAIS.values()), help=argparse.SUPPRESS)
    args = parser.parse_args()
    if args.arquivo:
        for linha in sys.stdin.buffer:
            try:
                pedido = json.loads(linha)
            except ValueError:
                pedido = {}
            if not isinstance(pedido, dict):
                pedido = {}
            dados = json.dumps(resposta_mcp(pedido, args.arquivo), ensure_ascii=True)
            print(dados, flush=True)
        return
    with HTTPServer(("127.0.0.1", 0), Rececao) as servidor:
        servidor.tarefas = {}
        thread = Thread(target=servidor.serve_forever, kwargs={"poll_interval": 0.05}, daemon=True)
        thread.start()
        try:
            resultados = verificar(servidor.server_port)
        finally:
            servidor.shutdown()
            thread.join()
    print(json.dumps({"mcp": MCP, "a2a": A2A, "verificacoes": resultados,
                      "total": len(resultados), "chamadas_llm": 0}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
