#from pocketsphinx import LiveSpeech
import string
import youtubeFetch
#import texttospeech
import petestts as texttospeech
import newsFetch
import dictionaryFetch
import reminders
import shopping
import wikipediaFetch
global openVideos
global reminderList
def speechRecognition():
    for phrase in LiveSpeech():
        if "assistant" in phrase:
            analyseSpeech(shortenSpeech(phrase))
def shortenSpeech(phrase):
    exclude = set(string.punctuation)
    phrase = phrase.lower()
    phrase = ''.join(ch for ch in phrase if ch not in exclude)
    phrase = phrase.split()
    found = False
    while found == False:
        if phrase[0] != "assistant":
            del(phrase[0])
        else:
            del(phrase[0])
            found = True
    return(phrase)
def analyseSpeech(phrase):
    #try:
        if phrase[0] == 'play' and len(phrase)>1:
            del(phrase[0])
            phrases = " ".join(x for x in phrase)
            youtubeFetch.getResults(phrases)
            texttospeech.tts(("now playing, ", phrases))
            try:
                openVideos += 1
            except:
                openVideos = 0
        elif "news" in phrase or "headlines" in phrase:
            texttospeech.tts("here is the news. . ")
            texttospeech.tts(newsFetch.getBBCNews())
        elif len(phrase) == 2 and (phrase[1] == "meaning" or phrase[1] == "definition"):
            texttospeech.tts(("the meaning of", phrase[0]))
            texttospeech.tts(dictionaryFetch.getMeaning(phrase[0]))
        elif len(phrase) == 2 and phrase[1] == "spelling":
            newphrase = "the spelling of " + phrase[0] + " is " + dictionaryFetch.getSpelling(phrase[0])
            texttospeech.tts(newphrase)
        elif len(phrase) == 1 and (phrase[0] == "play" or phrase[0] == "pause"):
            youtubeFetch.pausePlay()
            texttospeech.tts("okay")
        elif "reminder" in phrase:
            if "set" in phrase:
                texttospeech.tts("okay, what would you like me to set a reminder for")
                for phrase in LiveSpeech():
                    reminderList = reminders.addReminder(phrase, reminderList)
                    break
            elif "read" in phrase:
                texttospeech.tts("here are your reminders", reminders.readReminders())
        elif "shopping" in phrase:
            item = ""
            if phrase[0] == "add" and "to" in phrase:
                for i in range (len(phrase)):
                    item = " ".join(phrase[i])
                    if phrase[i] == "to":
                        break
                try:
                    shoppingList = shopping.addToList(shoppingList, item)
                except:
                    shoppingList = shopping.addToList(item)
                texttospeech.tts("added", item, "to shopping list")
            elif "read" in phrase:
                try:
                    texttospeech.tts(" ".join(x for x in shoppingList))
                except:
                    texttospeech.tts("you dont seem to have a shopping list")
            elif "add" in phrase:
                texttospeech.tts("what do you want to add to your shopping list?")
                for phrase in LiveSpeech():
                    try:
                        shoppingList = shopping.addToList(shoppingList, phrase)
                    except:
                        shoppingList = shopping.addToList(phrase)
                    texttospeech.tts("added", phrase, "to shopping list")
                    break
            elif "clear" in phrase:
                texttospeech.tts("do you want me to clear your shopping list")
                answered = False
                while answered == False:
                    for phrase in LiveSpeech():
                        if phrase == "yes":
                            shopping.clearShoppingList()
                            texttospeech.tts("cleared shopping list")
                            answered = True
                        elif phrase == "no":
                            texttospeech.tts("not cleared shopping lisst")
                            answered = True
        elif "wikipedia" in phrase or "wiki" in phrase:
            if "wikipedia" == phrase[0] or "wiki" == phrase[0]:
                del(phrase[0])
                phrases = " ".join(x for x in phrase)
                texttospeech.tts(wikipediaFetch.WikiFetch(phrases))
            elif "wikipedia" == phrase[len(phrase)-1] or "wiki" == phrase[len(phrase)-1]:
                del(phrase[len(phrase)-1])
                phrases = " ".join(x for x in phrase)
                texttospeech.tts(wikipediaFetch.WikiFetch(phrases))
            else:
                texttospeech.tts("sorry, I don't understand")



    #except:
        #return()
analyseSpeech(shortenSpeech("blah blah blah blhasdfgbdsv sdfbsd dxv assistant asdfghwijkjhgf wiki asdfghgf"))

