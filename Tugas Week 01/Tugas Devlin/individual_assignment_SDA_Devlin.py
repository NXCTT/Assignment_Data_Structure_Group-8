#INDIVIDUAL ASSIGNMENT T4
#Sum, Factorial, Fibonacci

# Nama = Devlin Manuel
# NIM = 232202935

import os

#buat 5 function:

def input_validate():
    user_input = []
    value = int(input(f"Input random numbers: "))
    user_input.append(value)
    mode = int(input(f"Choose your mode (1-3): "))
    user_input.append(mode)

    return user_input

def sum_mode(value):
    if value == 1:
        return value
    else:
        return value + sum_mode(value - 1)

def factorial_mode(value):
    if value == 1:
        return value
    else:
        return value * factorial_mode(value - 1)

def fibonacci_mode(value):
    if value <= 1:
        return value
    else:
        return fibonacci_mode(value - 1) + fibonacci_mode(value - 2)

def print_result(result_sum, result_fac, result_fib):
    if result_fac == "" and result_fib == "":
        print(f"Your sum count result is {result_sum}\n")
    elif result_sum == "" and result_fib == "":
        print(f"Your factorial count result is {result_fac}\n")
    elif result_sum == "" and result_fac == "":
        print(f"Your fibonacci count result is {result_fib}\n")

#MAIN FUNCTION:

def main_program():
    while True:
        os.system("cls")
        print(f"{'Welcome to Sum, factorial, and Fibonacci Program':^70}")
        print("")
        print(f"Choose your mode:")
        print(f"1 = Sum")
        print(f"2 = Factorial")
        print(f"3 = Fibonacci")
        print("")

        user_input = input_validate()
        print("")
        value = user_input[0]
        mode = user_input[1]
        print(f"~ your numbers = {value}")

        # untuk menentukan mode perhitungan:
        result_sum = ""
        result_fac = ""
        result_fib = ""

        if mode == 1:
            print(f"~ your mode = sum")    
            result_sum = sum_mode(value)
        elif mode == 2:
            print(f"~ your mode = factorial")    
            result_fac = factorial_mode(value)
        elif mode == 3:
            print(f"~ your mode = fibonacci")    
            result_fib = fibonacci_mode(value)
        
        #untuk menampilkan hasil perhitungan
        print("")
        print_result(result_sum, result_fac, result_fib)

        #untuk menentukan lanjut atau stop:
        next_count = int(input(f"Want to count the other(y = 0, n = -1)? "))
        if next_count == 0:
            continue
        elif next_count == -1:
            break


main_program()