import re
import random

def detectar_agradecimento(comando):
    padrao = re.compile(r"\b(obrigado|obrigada|valeu|agradeço|grato|grata)\b", re.IGNORECASE)
    return bool(padrao.search(comando))

def responder_agradecimento():
    respostas = [
        "Conte comigo, estou aqui para ajudar!",
        "De nada! Se precisar de mais alguma coisa, é só chamar.",
        "Tamo junto!",
        "É nóis!",
        "É nóis que voa, bruxão!",
        "Sempre um prazer servir.",
        "Por nada, guerreiro do código.",
        "A LucIA sempre responde a chamados dignos."
    ]
    return random.choice(respostas)
