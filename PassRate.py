def getValue():
    value = input()
    try:
        value = int(value)
    except:
        print("Incorrect value. Try again!")
        value = getValue()

    if value < 0:
        print("Incorrect value. Try again!")
        value = getValue()

    return value


def passRateCount(allTasks, passedTasks):
    passRate = passedTasks/allTasks*100
    return passRate


print("Input all tasks count: ")
allTasks = getValue()
print("Input passed tasks count: ")
passedTasks = getValue()
passRate = passRateCount(allTasks, passedTasks)
print("Pass rate: %0.2f" % passRate)
