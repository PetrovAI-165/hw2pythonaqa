def getMeasureUnit():
    allowedUnits = ['C', 'F', 'K']
    measureUnit = input().upper()
    try:
        allowedUnits.index(measureUnit.upper())
    except:
        print("Incorrect value. Try again!")
        measureUnit = getMeasureUnit()

    return measureUnit


def getValue():
    incomingValue = input()
    try:
        incomingValue = float(incomingValue)
    except:
        print("Not a number. Try again!")
        incomingValue = getValue()

    return incomingValue


def temperatureExchange(incomingValue, expectedMeasureUnit):
    if expectedMeasureUnit.upper() == 'C':
        return incomingValue
    elif expectedMeasureUnit.upper() == 'K':
        return incomingValue + 273.2
    elif expectedMeasureUnit.upper() == 'F':
        return incomingValue * 1.8 + 32
    else:
        return None


print("Input temp:")
incomingValue = getValue()
print("Input your measure unit (C, F, K):")
expectedMeasureUnit = getMeasureUnit()
print("%0.2f in C equal to %0.2f in %s" % (incomingValue,
                                           temperatureExchange(incomingValue, expectedMeasureUnit),
                                           expectedMeasureUnit))
