print("Factorial of a number")

# n! = n * (n-1) * (n-2) .... 1
# 4! = 4 * 3 * 2 * 1 = 24

number = int(input("Enter the number: "))


def factorial_num(param):
    factorial_result = 1

    while (param > 0):
        factorial_result *= param
        param -= 1
    return factorial_result


result = factorial_num(number)
print(f"The factorial of a number {number} is {result}")
