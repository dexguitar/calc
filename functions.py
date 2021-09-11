def addition(x, y):
    print("{:.2f}".format(float(x) + float(y)), "Yyyees!")


def subtraction(x, y):
    sub = float(x) - float(y)
    if sub < 0:
        print("Can't subtract")
    else:
        print("{:.2f}".format(float(x) - float(y)), "Wow")


def multiplication(x, y):
    print("{:.2f}".format(float(x) * float(y)), "Uhhuuu!")


def division(x, y):
    if int(y) == 0:
        print("ooo shit! can't do that!")
    else:
        print("{:.2f}".format(float(x) / float(y)), "Uhhuuu!")
