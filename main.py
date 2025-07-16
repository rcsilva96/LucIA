import threading
from core.voice import falar, ouvir_microfone
from core.commands import executar_comando
from interface.avatar import iniciar_interface

falar("Olá! Eu sou a LucIA. Diga meu nome para ativar.")

# Iniciar avatar em paralelo
threading.Thread(target=iniciar_interface, daemon=True).start()

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
        continue