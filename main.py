from functions import *

if __name__ == '__main__':
    first = input("Input first number: ")
    second = input("Input second number: ")
    third = input("Input what you gonna do?: ")

    if third == "+":
        print(addition(first, second))
    if third == "-":
        print(subtraction(first, second))
    if third == "*":
        print(multiplication(first, second))
    if third == "/":
        print(division(first, second))
