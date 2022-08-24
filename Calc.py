def getValue():
    value = input()
    try:
        value = float(value)
    except:
        print("Not a number. Try again!")
        value = getValue()

    return value


def getOperand():
    allowedOperands = ['-', '+', '/', '*']
    operand = input()
    try:
        allowedOperands.index(operand)
    except:
        print("Incorrect value. Try again!")
        operand = getOperand()

    return operand


def calc(firstValue, operand, secondValue):
    if secondValue == 0:
        actions = {
            '+': firstValue,
            '-': firstValue,
            '*': 0,
            '/': None
        }
        return actions.get(operand)

    actions = {
        '+': firstValue + secondValue,
        '-': firstValue - secondValue,
        '*': firstValue * secondValue,
        '/': firstValue / secondValue
    }

    return actions.get(operand)


print("Input value: ")
firstValue = getValue()
print("Input action: ")
operand = getOperand()
print("Input value: ")
secondValue = getValue()
result = calc(firstValue, operand, secondValue)
print("%0.2f %s %0.2f = %0.2f" % (firstValue, operand, secondValue, result))