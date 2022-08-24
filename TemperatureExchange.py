def getMeasureUnit():
    allowedUnits = ['C', 'F', 'K']
    print("Input your measure unit (C, F, K):")
    measureUnit = input()

    try:
        allowedUnits.index(measureUnit)
    except:
        print("Incorrect value. Try again!")
        measureUnit = getMeasureUnit()

    return measureUnit


def getValue():
    print("Input temp:")
    incomingValue = input()
    try:
        incomingValue = float(incomingValue)
    except:
        print("Not a number. Try again!")
        incomingValue = getValue()
    return incomingValue


def temperatureExchange(incomingValue, expectedMeasureUnit):
    if expectedMeasureUnit == 'C':
        return incomingValue
    elif expectedMeasureUnit == 'K':
        return incomingValue + 273.2
    elif expectedMeasureUnit == 'F':
        return incomingValue * 1.8 + 32
    else:
        return None


incomingValue = getValue()
expectedMeasureUnit = getMeasureUnit()
print("%0.2f in C equal to %0.2f in %s" % (incomingValue,
                                    temperatureExchange(incomingValue, expectedMeasureUnit),
                                    expectedMeasureUnit))
