from art import logo
from os import system, name


def clear():
    # cls for windows, posix for mac or linux
    system('cls') if name == 'nt' else system('clear')


print(logo)


def add(n1, n2):
    return n1+n2


def subtract(n1, n2):
    return n1-n2


def multiply(n1, n2):
    return n1*n2


def divide(n1, n2):
    return n1/n2


def main():
    while True:
        first_number = float(input("What is the first number?: "))
        print("+\n-\n*\n/\n")
        continue_calculation = True
        while continue_calculation:
            calc_operation = input("Pick an operation: ")
            next_number = float(input("What is the next number?: "))
            if calc_operation == "+":
                answer = add(first_number, next_number)
                print(f"{first_number} + {next_number} = {answer}")
            elif calc_operation == "-":
                answer = subtract(first_number, next_number)
                print(f"{first_number} - {next_number} = {answer}")
            elif calc_operation == "*":
                answer = multiply(first_number, next_number)
                print(f"{first_number} * {next_number} = {answer}")
            elif calc_operation == "/":
                answer = divide(first_number, next_number)
                print(f"{first_number} / {next_number} = {answer}")
            first_number = answer
            continue_calc = input(f"Type 'y' to continue calculating with {first_number}, or type 'n' to start a new calculation: ")
            if continue_calc == 'n':
                continue_calculation = False
                clear()


if __name__ == '__main__':
    main()

