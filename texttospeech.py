import pyttsx3
import time


def tts(text):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')  # getting details of current speaking rate
    print(rate)  # printing current voice rate
    engine.setProperty('rate', 150)  # setting up new voice rate
    engine.say(text)
    engine.runAndWait()
