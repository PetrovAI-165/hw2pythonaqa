def getValue():
    incomingValue = input()
    try:
        incomingValue = float(incomingValue)
    except:
        print("Not a number. Try again!")
        incomingValue = getValue()

    if incomingValue < 0:
        print("Incorrect value. Try again")
        incomingValue = getValue()

    return incomingValue


def getCurrency():
    allowedCurrency = ['UAH', 'USD', 'EUR']
    currency = input().upper()
    try:
        allowedCurrency.index(currency.upper())
    except:
        print("Incorrect value. Try again!")
        currency = getCurrency()

    return currency


def exchange(inCurrency, inValue, outCurrency):
    currencyPair = {
        ("UAH", "USD"): 0.025,
        ("USD", "UAH"): 40,
        ("EUR", "UAH"): 42,
        ("UAH", "EUR"): 0.0238
    }

    coef = currencyPair.get((inCurrency, outCurrency))

    if coef is None:
        print("Not allowed pair")
        exit()

    return inValue*coef


print("Your currency: ")
inCurrency = getCurrency()
print("Your value: ")
inValue = getValue()
print("Convert to: ")
outCurrency = getCurrency()
outValue = exchange(inCurrency, inValue, outCurrency)
print("%0.2F %s = %0.2f %s" % (inValue, inCurrency, outValue, outCurrency))
