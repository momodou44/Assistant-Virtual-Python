import speech_recognition as sr   #permet a la machine de reconnaitre ce qu'on dit
import pyttsx3 as ttx    #permet a la machine de parler
import pywhatkit
import datetime

listener = sr.Recognizer()  #permt a la machine d'ecouter
engine=ttx.init()
voice=engine.getProperty('voices')
engine.setProperty('voice','french')


def parler(text):
    engine.say(text)
    engine.runAndWait()


def ecouter():
    try:
        with sr.Microphone() as source:
            print("Parler Maintenant")
            voix=listener.listen(source)
            command= listener.recognize_google(voix,language='fr-FR')
            command.lower()
    except:
        pass
    return command

def lancer_assistant():
    command = ecouter()
    print(command)

    if 'mets la chanson de ' in command:
        chanteur=command.replace('mets la chanson de','')
        print(chanteur)
        #parler(chanteur)
        parler('d\'accord')
        pywhatkit.playonyt(chanteur)
    elif 'heure' in command:
        heure=datetime.datetime.now().strftime('%H:%M')
        parler('il est '+heure)
    elif 'Bonjour' in command:
        parler('bonjour, ca va ?')
    elif 'nom' in command:
        parler('Ousmane')
    elif 'champions d\'Afrique' in command:
        parler('Le Senegal')
    else:
        parler('je ne comprends pasa')

while True:
    lancer_assistant()