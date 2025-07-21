# Utilidade independente para listar arquivos e diretórios de forma hierárquica, não relacionada à LucIA

import os

def listar_arquivos(diretorio, prefixo=""):
    arquivos = sorted(os.listdir(diretorio))
    for i, nome in enumerate(arquivos):
        caminho_completo = os.path.join(diretorio, nome)
        conector = "└── " if i == len(arquivos) - 1 else "├── "
        print(prefixo + conector + nome)
        if os.path.isdir(caminho_completo):
            novo_prefixo = prefixo + ("    " if i == len(arquivos) - 1 else "│   ")
            listar_arquivos(caminho_completo, novo_prefixo)

if __name__ == "__main__":
    listar_arquivos(".")