print("add two numbers")

num1 = int(input("First Number: "))
num2 = int(input("Second Number: "))


def add_two_numbers(param1, param2):
    return param1 + param2


result = add_two_numbers(num1, num2)
print(f"The sum of {num1} & {num2} is {result}")
