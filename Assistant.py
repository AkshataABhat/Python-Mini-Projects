import pyttsx3  #pip install pyttsx3
import datetime
import speech_recognition as sr

engine=pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time_():
    Time=datetime.datetime.now().strftime("%H:%M:%S")
    speak("The time now is")
    speak(Time)

def date_():
    year=datetime.datetime.now().year
    month=datetime.datetime.now().month
    date=datetime.datetime.now().day
    speak("Today's date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak('Welcome back, (Your Name).')
    time_()
    date_()

    hour=datetime.datetime.now().hour

    if hour>=0 and hour<12:
        speak('Good Morning, (Your Name). Have a nice day!') 
    if hour>=12 and hour<18:
        speak('Good Afternoon, (Your Name).')
    if hour>=18 and hour<24:
        speak('Good evening.')
    else :
        speak('Good Night.')

    speak('How can I help you today?')

wishme()
