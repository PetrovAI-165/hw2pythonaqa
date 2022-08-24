def getVolume():
    volume = input()
    try:
        volume = float(volume)
    except:
        print("Not a number. Try again!")
        volume = getVolume()

    if volume < 0:
        print("Incorrect value. Try again!")
        volume = getVolume()

    return volume


def getTemp():
    temp = input()
    try:
        temp = float(temp)
    except:
        print("Not a number. Try again!")
        temp = getTemp()

    return temp


def mixTempCalc(firstVolume, firstTemp, secondTemp, secondVolume):
    return (firstTemp * firstVolume + secondVolume * secondTemp)/(firstVolume+secondVolume)


print("First volume: ")
firstVolume = getVolume()
print("First temp: ")
firstTemp = getTemp()
print("Second volume: ")
secondVolume = getVolume()
print("Second temp: ")
secondTemp = getTemp()
resultVolume = firstVolume + secondVolume
print("Mix volume: %0.2f. Mix temp: %0.2f" % (resultVolume,
                                              mixTempCalc(firstVolume, firstTemp, secondTemp, secondVolume)))
