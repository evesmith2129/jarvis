import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)

def wishme():
    speak("Welcome back sir!")
    time_()
    date_()

    hour = datetime.datetime.now().hour

    if hour >= 6 and hour < 12:
        speak("Good morning sir!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon sir!")
    elif hour >= 18 and hour < 24:
        speak("Good evening sir!")
    else:
        speak("Good night sir!")
    
    speak("Jarvis at your service. Please tell me how can I help you today?")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time_():
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)

def date_():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)

def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-US')
        print(query)

    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "None"

    return query

if __name__ == "__main__":
    input("Press Enter to continue...")
    wishme()
    while True:
        if "wikipedia"in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)