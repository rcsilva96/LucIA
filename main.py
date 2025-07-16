import speech_recognition as sr
import pyttsx3
import webbrowser
import pyautogui
import subprocess
import time
import requests
from datetime import datetime

# Configurações iniciais
nome_assistente = "lúcia"
ativado = False

# Inicializa o reconhecedor de voz e o sintetizador de fala
reconhecedor = sr.Recognizer()
engine = pyttsx3.init()

# Configurações de voz
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 180)  # Velocidade da fala

# Caminhos dos programas (ajuste conforme seu sistema)
CAMINHOS = {
    'calculadora': 'C:\\Windows\\System32\\calc.exe',
    'vscode': 'C:\\Users\\Renato\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe',
    'navegador': 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
    'bloco_de_notas': 'C:\\Windows\\System32\\notepad.exe'
}

# Core da LucIA - Ouvir, falar e executar comandos

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
        audio = reconhecedor.listen(source, timeout=5)

    try:
        texto = reconhecedor.recognize_google(audio, language='pt-BR').lower()
        print(f"Você disse: {texto}")
        return texto
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        falar("Desculpe, estou com problemas no serviço de voz.")
        return ""
    except sr.WaitTimeoutError:
        return ""

def abrir_programa(caminho):
    """Abre um programa de forma robusta"""
    try:
        subprocess.Popen(caminho)
        return True
    except Exception as e:
        print(f"Erro ao abrir programa: {e}")
        return False

def executar_comando(comando):
    """Executa ações baseadas no comando de voz"""
    global ativado

    if not ativado and nome_assistente in comando:
        if "bom dia" in comando:
            ativado = True
            falar("Olá, bom dia! Como posso ajudar?")
            return
        elif "boa tarde" in comando:
            ativado = True
            falar("Olá, boa tarde! Como posso ajudar?")
            return
        elif "boa noite" in comando:
            ativado = True
            falar("Olá, boa noite! Como posso ajudar?")
            return
        else:
            ativado = True
            falar("Olá, como posso te ajudar?")
            return

    if ativado:
        if "parar" in comando or "sair" in comando:
            falar("Até logo!")
            ativado = False

        # Comandos e ferramentas padrões do Windows

        elif "abrir calculadora" in comando or "calculadora" in comando:
            if abrir_programa(CAMINHOS['calculadora']):
                falar("Calculadora aberta.")
            else:
                falar("Não consegui abrir a calculadora.")

        elif "abrir bloco de notas" in comando or "notepad" in comando:
            if abrir_programa(CAMINHOS['bloco_de_notas']):
                falar("Bloco de notas aberto.")
            else:
                falar("Não consegui abrir a calculadora.")

        elif "escrever" in comando:
            texto_para_escrever = comando.replace("escrever", "").strip()
            pyautogui.write(texto_para_escrever, interval=0.1)
            falar("Pronto, escrevi o que você pediu.")

        elif "abrir navegador" in comando:
            if abrir_programa(CAMINHOS['navegador']):
                falar("Navegador aberto.")
            else:
                webbrowser.open('https://www.google.com')
                falar("Abrindo navegador padrão.")

        elif ("pesquise na internet") in comando:
            termo = comando.split("pesquise na internet")[-1].strip()
            webbrowser.open('https://www.google.com/search?1={termo}')

        elif "fechar janela" in comando:
            pyautogui.hotkey('alt', 'f4')
            falar("Janela fechada.")

        # Ferramentas  de desenvolvimento

        elif "hora do show" in comando:
            if abrir_programa(CAMINHOS['vscode']):
                falar("Bora codificar!")
            else:
                falar("Não encontrei o Visual Studio Code.")

        # Pesquisas e informações

        elif "cotação do dólar" in comando or "valor do dólar" in comando:
            dados_cotacao = obter_cotacao_dolar()
            if dados_cotacao:
                mensagem = (f"A cotação atual do dólar é R$ {dados_cotacao['cotacao']:.2f}. "
                            f"Variação de {dados_cotacao['variacao']:.2f}%.")
                falar(mensagem)
            else:
                falar("Não consegui obter a cotação do dólar no momento.")

        # Interações e comandos adicionais

        elif "obrigado" in comando or "obrigada" in comando:
            falar("Conte comigo! Estou aqui para ajudar.")

        # Adicione mais comandos aqui
        else:
            falar("Desculpe, não entendi o comando.")

# Funções com APIs externas

def obter_cotacao_dolar():
    """Obtém a cotação atual do dólar usando a API do Banco Central"""
    try:
        # API do Banco Central (dólar comercial)
        url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
        response = requests.get(url)
        dados = response.json()

        cotacao = float(dados['USDBRL']['bid'])
        variacao = float(dados['USDBRL']['varBid'])
        hora_consulta = dados['USDBRL']['create_date']

        return {
            'cotacao': cotacao,
            'variacao': variacao,
            'hora': hora_consulta
        }
    except Exception as e:
        print(f"Erro ao obter cotação: {e}")
        return None


# Inicialização
falar(f"Olá! Eu sou a LucIA. Diga meu nome para ativar.")

# Loop principal
while True:
    try:
        comando = ouvir_microfone()
        if comando:
            executar_comando(comando)
    except KeyboardInterrupt:
        falar("Encerrando a LucIA.")
        break
    except Exception as e:
        print(f"Erro: {e}")
        time.sleep(1)