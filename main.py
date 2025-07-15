import speech_recognition as sr
import pyttsx3
import os
import webbrowser
import pyautogui
import numpy as np

# Configurações iniciais
nome_assistente = "lúcia"
ativado = False

# Inicializa o reconhecedor de voz e o sintetizador de fala
reconhecedor = sr.Recognizer()
engine = pyttsx3.init()

# Configura a voz (opcional - depende das vozes instaladas no sistema)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Seleciona a primeira voz disponível


def falar(texto):
    """Faz o assistente falar o texto"""
    print(f"LucIA: {texto}")
    engine.say(texto)
    engine.runAndWait()


def ouvir_microfone():
    """Ouve o microfone e retorna o texto reconhecido"""
    with sr.Microphone() as source:
        print("Aguardando comando...")
        reconhecedor.adjust_for_ambient_noise(source)
        audio = reconhecedor.listen(source)

    try:
        texto = reconhecedor.recognize_google(audio, language='pt-BR').lower()
        print(f"Você disse: {texto}")
        return texto
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        falar("Desculpe, estou com problemas no serviço de voz.")
        return ""


def executar_comando(comando):
    """Executa ações baseadas no comando de voz"""
    global ativado

    if not ativado and nome_assistente in comando:
        ativado = True
        falar("Sim, como posso ajudar?")
        return

    if ativado:
        if "parar" in comando or "sair" in comando:
            falar("Até logo!")
            ativado = False
        elif "abrir calculadora" in comando:
            os.system('calc.exe')
            falar("Calculadora aberta.")
        elif "abrir navegador" in comando:
            webbrowser.open('https://www.google.com')
            falar("Navegador aberto.")
        elif "pesquisar" in comando:
            termo = comando.replace("pesquisar", "").strip()
            if termo:
                webbrowser.open(f'https://www.google.com/search?q={termo}')
                falar(f"Pesquisando por {termo}")
        # Adicione mais comandos aqui conforme necessário
        else:
            falar("Desculpe, não entendi o comando.")


# Loop principal
falar(f"Olá! Eu sou a {nome_assistente}. Diga meu nome para ativar.")
while True:
    comando = ouvir_microfone()
    if comando:
        executar_comando(comando)