print("Program to check whether a number is prime or not")


number = int(input("Enter the number: "))


def check_prime_or_not(num):
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i == 0):
                print(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number")
    else:
        print(num, "is not a prime number")


check_prime_or_not(number)
