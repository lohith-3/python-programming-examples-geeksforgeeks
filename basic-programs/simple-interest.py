print("Program for simple interest")


# SI = (P * T * R) / 100
# P is the principal amount
# T is the Time
# R is the rate

principal_amount = int(input("Enter the principal amount: "))
time = int(input("Enter the time: "))
rate = int(input("Enter the rate: "))


def simple_interest(principal_amount, time, rate):
    si = (principal_amount * time * rate) / 100
    return si


result = simple_interest(principal_amount, time, rate)
print("The simple interest is {}".format(result))
