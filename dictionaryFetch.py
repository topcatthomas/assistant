from PyDictionary import PyDictionary
def getMeaning(word):
    dictionary=PyDictionary()
    return(dictionary.meaning(word))
def getSpelling(word):
    spelling = []
    for i in range (len(word)):
        spelling.append(word[i])
    word = " ".join(x for x in spelling)
    return(word)