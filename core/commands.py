from core.voice import falar, nome_assistente
from core.utils import abrir_programa, obter_cotacao_dolar, CAMINHOS
import pyautogui
import webbrowser

ativado = False

def executar_comando(comando):
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

        elif "abrir calculadora" in comando or "calculadora" in comando:
            falar("Abrindo calculadora.") if abrir_programa(CAMINHOS['calculadora']) else falar("Não consegui abrir a calculadora.")

        elif "abrir bloco de notas" in comando or "notepad" in comando:
            falar("Abrindo bloco de notas.") if abrir_programa(CAMINHOS['bloco_de_notas']) else falar("Não consegui abrir.")

        elif "escrever" in comando:
            texto_para_escrever = comando.replace("escrever", "").strip()
            pyautogui.write(texto_para_escrever, interval=0.1)
            falar("Pronto, escrevi o que você pediu.")

        elif "abrir navegador" in comando:
            falar("Abrindo navegador.") if abrir_programa(CAMINHOS['navegador']) else webbrowser.open('https://www.google.com')

        elif "pesquise na internet" in comando:
            termo = comando.split("pesquise na internet")[-1].strip()
            webbrowser.open(f'https://www.google.com/search?q={termo}')

        elif "fechar janela" in comando:
            pyautogui.hotkey('alt', 'f4')
            falar("Janela fechada.")

        elif "hora do show" in comando:
            falar("Bora codar!") if abrir_programa(CAMINHOS['vscode']) else falar("Não encontrei o VS Code.")

        elif "cotação do dólar" in comando or "valor do dólar" in comando:
            dados = obter_cotacao_dolar()
            if dados:
                falar(f"A cotação atual do dólar é R$ {dados['cotacao']:.2f}. Variação de {dados['variacao']:.2f}%.")
            else:
                falar("Não consegui obter a cotação agora.")

        elif "obrigado" in comando or "obrigada" in comando:
            falar("Conte comigo! Estou aqui para ajudar.")

        else:
            falar("Desculpe, não entendi o comando.")