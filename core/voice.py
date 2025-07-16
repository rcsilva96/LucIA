import speech_recognition as sr
import pyttsx3

reconhecedor = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 180)

nome_assistente = "lúcia"

def falar(texto):
    print(f"LucIA: {texto}")
    engine.say(texto)
    engine.runAndWait()

def ouvir_microfone():
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