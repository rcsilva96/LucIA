import subprocess
import requests
import pyautogui
import webbrowser

CAMINHOS = {
    'calculadora': 'C:\\Windows\\System32\\calc.exe',
    'vscode': 'C:\\Users\\Renato\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe',
    'navegador': 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
    'bloco_de_notas': 'C:\\Windows\\System32\\notepad.exe'
}

def abrir_programa(caminho):
    try:
        subprocess.Popen(caminho)
        return True
    except Exception as e:
        print(f"Erro ao abrir programa: {e}")
        return False