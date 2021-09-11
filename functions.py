def addition(x, y):
    return "{:.2f}".format(float(x) + float(y))


def subtraction(x, y):
    sub = float(x) - float(y)
    if sub < 0:
        return "Can't subtract"
    else:
        return "{:.2f}".format(float(x) - float(y))


def multiplication(x, y):
    return "{:.2f}".format(float(x) * float(y))


def division(x, y):
    if int(y) == 0:
        return "ooo shit! can't do that!"
    else:
        return "{:.2f}".format(float(x) / float(y))
