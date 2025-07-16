# skills/lembrete.py

import re
import datetime
from plyer import notification
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()
scheduler.start()

def parse_lembrete(comando):
    # Remove o trecho final do tipo "em 10 segundos", "em 5 minutos", etc.
    match = re.search(r"me lembre de (.+?) em \d+ ?(segundos|minutos|horas?)", comando, re.IGNORECASE)
    if match:
        return match.group(1).strip()
    else:
        # fallback, pega tudo depois de "me lembre de"
        return comando.split("me lembre de")[-1].strip()

def parse_tempo(comando):
    # Regex esperta: "em 10 segundos/minutos/horas"
    match = re.search(r"em (\d+)\s*(segundos|minutos|horas?)", comando, re.IGNORECASE)
    if match:
        valor = int(match.group(1))
        unidade = match.group(2).lower()
        agora = datetime.datetime.now()

        if "seg" in unidade:
            return agora + datetime.timedelta(seconds=valor)
        elif "min" in unidade:
            return agora + datetime.timedelta(minutes=valor)
        elif "hora" in unidade:
            return agora + datetime.timedelta(hours=valor)
    return None

def notificar(titulo, mensagem):
    notification.notify(
        title=titulo,
        message=mensagem,
        app_name="LucIA",
        timeout=10
    )

def can_handle(comando):
    return "me lembre" in comando.lower()

def execute(comando):
    tempo = parse_tempo(comando)
    if tempo:
        mensagem = parse_lembrete(comando)
        scheduler.add_job(
            lambda: notificar("Lembrete da LucIA", mensagem),
            trigger='date',
            run_date=tempo
        )
        return f"Ok! Vou te lembrar de '{mensagem}'!"
    else:
        return "Desculpe, não entendi o tempo do lembrete."

