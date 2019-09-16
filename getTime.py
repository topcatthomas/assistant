import datetime
def returnTime():
    now = datetime.datetime.now()
    return("the time is, " + str(datetime.time(now.hour, now.minute)))
