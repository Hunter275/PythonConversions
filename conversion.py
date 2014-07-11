#Converts temperature between Celcius, Kelvin, and Fahrenheit
def temp(scaleinit, scalefinal, number):
    if scaleinit.upper() == "F":
        if scalefinal.upper() == "C":
            return ((number - 32) / 1.8)
        elif scalefinal.upper() == "K":
            return (((number - 32) / 1.8) + 273.15)
        else:
            return "Broke"

    elif scaleinit.upper() == "C":
        if scalefinal.upper() == "F":
            return (((number - 273.15) * 1.8) + 32)
        elif scalefinal.upper() == "K":
            return (number + 273.15)
        else:
            return "Broke"

    elif scaleinit.upper() == "K":
        if scalefinal.upper() == "F":
            return (((number - 273.15) * 1.8) + 32)
        elif scalefinal.upper() == "C":
            return (number - 273.15)
        else:
            return "Broke"


#Coverts between data sizes, base 2 (1024)
def data(datainit, datafinal, number):
    scale = {"byte": 1, "kb": 2, "mb": 3, "gb": 4, "tb": 5, "pb": 6}
    return (number / (1024.0**(scale[datafinal] - scale[datainit])))


#Coverts between US timezones
def timezone(local, remote, time):
    timezones = {"HST": 6, "AST": 5, "PST": 4, "MST": 3, "CST": 2, "EST": 1}
    timeraw = time.split(':')
    hour = timeraw[0]
    return str(hour + (timezones[local.upper()] - timezones[remote.upper()])) + ":" + time[3:5] + " " + remote.upper()


#Converts between metric weights, allows for US pounds
def weight(baseinit, basefinal, number):
    if baseinit == "lbs":
        number = number * 2.2
        baseinit = "kg"
    zeros = ""
    point = 1
    metric = {"mg": 1, "cg": 2, "dg": 3, "g": 4, "dag": 5, "hg": 6, "kg": 7}
    while point <= ((metric[basefinal] - metric[baseinit])):
        zeros = zeros + "0"
        point = point + 1
    return str(number * int("1" + zeros)) + " " + basefinal.upper()


#Converts between feet, miles, inches, and the basic metric distances
def distance(baseinit, basefinal, number):
    zeros = ""
    point = 1
    us = {"inch": 1/12.0, "foot": 1, "yard": 3, "mile": 5280}
    metric = {"mm": 1, "cm": 2, "dm": 3, "m": 4, "dam": 5, "hm": 6, "km": 7}
    while point <= ((metric[basefinal] - metric[baseinit])):
        zeros = zeros + "0"
        point = point + 1
    return str(number * int("1" + zeros)) + " " + basefinal.upper()

def time(time, delta):
    timeraw = time.split(':')
    hour = timeraw[0]
    minute = timeraw[1]

    deltaraw = delta.split(':')
    deltahour = deltaraw[0]
    deltaminute = deltaraw[1]

    finalhour = int(hour) + int(deltahour)
    finalminute = int(minute) + int(deltaminute)

    if finalminute > 59:
        print "This"
        finalminute = str(finalminute - 60).zfill(2)
        finalhour = finalhour + 1

    if finalhour > 12:
        finalhour = finalhour - 12

    return str(finalhour) + ":" + finalminute

print time("2:30", "1:93")


