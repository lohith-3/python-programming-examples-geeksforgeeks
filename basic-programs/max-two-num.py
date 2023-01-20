print("maximum of two numbers")


num1 = int(input("First Number: "))
num2 = int(input("Second Number: "))


def max_two_numbers(param1, param2):
    if (param1 > param2):
        return param1
    return param2


max_number = max_two_numbers(num1, num2)
print(f"The maximum of {num1} & {num2} is {max_number}")
