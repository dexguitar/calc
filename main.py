from functions import *

if __name__ == '__main__':
    first = input("Input first number: ")
    second = input("Input second number: ")
    third = input("Input what you gonna do?: ")

    if third == "+":
        addition(first, second)
    if third == "-":
        subtraction(first, second)
    if third == "*":
        multiplication(first, second)
    if third == "/":
        division(first, second)
