import petestts as tts
tts.tts( "hello pal, this is your raspberyr pi speaking, can you hear it?")



import pyttsx3
engine = pyttsx3.init()
engine.setProperty('volume', 0.9)
engine.say("hello pal, this is your raspberyr pi speaking, can you hear it?")
engine.runAndWait()
voices = engine.getProperty('voices')
for voice in voices:
    print(voice, voice.id)
    engine.setProperty('voice', voice.id)
#    engine.say("Hello World!")
#    engine.runAndWait()
#    engine.stop()

