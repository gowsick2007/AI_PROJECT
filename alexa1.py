import speech_recognition as sr
import pywhatkit
import pyttsx3
import datetime
import wikipedia
import pyjokes
import json
from urllib.request import urlopen

engine = pyttsx3.init()
listener = sr.Recognizer()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.upper()
            if 'ALEXA' in command:
                command = command.replace('ALEXA', '')
                print(command)
    except:
        pass
    return command


def run_command():
    command = take_command()
    if 'PLAY' in command:
        song = command.replace('PLAY', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'TIME' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        print(time)
        talk('current time is ' + time)
    elif 'WHO IS' in command:
        person = command.replace('WHO IS', '')
        info = wikipedia.summary(person, 3)
        print(info)
        talk(info)
    elif 'JOKE' in command:

        talk(pyjokes.get_joke())
    elif 'location' in command:
        url = 'http://ipinfo.io/json'
        response = urlopen(url)
        data = json.load(response)

        talk(data['city'])
        print(data['city'])
    else:
        talk('can you please tell agin')


while True:
    run_command()