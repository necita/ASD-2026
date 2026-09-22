from ollama import chat

MAX_PASSOS = 5
MODELO = "qwen3:4b"


# Tool sem parâmetro
def consultar_horario():
    """Consulta o horário atual do hospital."""
    return "O horário atual do hospital é 14:30."


# Tool com parâmetro
def consultar_sala(sala):
    """faz uma consulta"""
    salas = {
        "101": "Sala 101 - Primeiro andar",
        "102": "Sala 102 - Primeiro andar",
        "203": "Sala 203 - Segundo andar",
    }

    return salas.get(sala, f"A sala {sala} não foi encontrada.")


# Descrição das ferramentas para o modelo
tools = [
    {
        "type": "function",
        "function": {
            "name": "consultar_horario",
            "description": "Consulta o horário atual do hospital.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "consultar_sala",
            "description": "Consulta a localização de uma sala específica do hospital.",
            "parameters": {
                "type": "object",
                "properties": {
                    "sala": {
                        "type": "string",
                        "description": "Número da sala que deseja consultar."
                    }
                },
                "required": ["sala"]
            }
        }
    }
]


def executar_tool(nome, argumentos):
    if nome == "consultar_horario":
        return consultar_horario()

    if nome == "consultar_sala":
        return consultar_sala(argumentos.get("sala"))

    return "Ferramenta desconhecida."


def executar_agente(pergunta):

    mensagens = [
        {
            "role": "user",
            "content": pergunta
        }
    ]

    for passo in range(1, MAX_PASSOS + 1):

        print(f"\n--- PASSO {passo} ---")

        resposta = chat(
            model=MODELO,
            messages=mensagens,
            tools=tools
        )

        if not resposta.message.tool_calls:
            print("Resposta:", resposta.message.content)
            return passo

        for chamada in resposta.message.tool_calls:

            nome = chamada.function.name
            argumentos = chamada.function.arguments

            print("Ferramenta escolhida:", nome)
            print("Argumentos:", argumentos)

            resultado = executar_tool(nome, argumentos)

            print("Resultado:", resultado)

            return passo

    return MAX_PASSOS


if __name__ == "__main__":

    pergunta = input("\nFaça uma pergunta: ")

    passos = executar_agente(pergunta)

    print("\n==============================")
    print("PASSOS UTILIZADOS:", passos)