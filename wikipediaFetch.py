import wikipedia
def WikiFetch(searchThing):
    try:
        searchThing = wikipedia.search(searchThing)[0]
        value = wikipedia.summary(searchThing)
    except:
        try:
            searchThing = wikipedia.search(searchThing)[1]
            value = wikipedia.summary(searchThing)
        except:
            try:
                searchThing = wikipedia.search(searchThing)[2]
                value = wikipedia.summary(searchThing)
            except:
                value = "sorry, something went wrong."
    return(value)