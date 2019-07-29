from googlesearch import search
import webbrowser
import keyboard
import os
import time
def playYoutube(url):
    webbrowser.open_new_tab(url)
def getResults(query):
    result = "oops"
    for url in search(query + " youtube.com",stop=20):
        if "https://www.youtube.com/watch?v=" not in url:
            pass
        else:
            result = url
            break
    playYoutube(result)
def pausePlay():
    keyboard.press_and_release('space')
def clearTabs():
    os.system("TASKKILL /F /IM chrome.exe")
    webbrowser.open_new_tab("http://www.google.com")