def tts(txt):
    import os
    os.system('espeak -ven "{0}" --stdout | aplay'.format(txt))

