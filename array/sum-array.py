print("Program to find sum of array")

arr = [1, 2, 3]


def sum_array(array):
    sum = 0
    for i in array:
        sum += i
    return sum


sum = sum_array(arr)
print(f"The sum of array is {sum}")
