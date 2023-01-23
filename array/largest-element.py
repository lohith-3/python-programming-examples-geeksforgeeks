print("Program to find largest element in an array")


arr = [20, 10, 20, 4, 100]


def largest_element(array):
    maximum = 0

    for i in array:
        if (maximum < i):
            maximum = i
    return maximum


maximum_element = largest_element(arr)

print(f"The maximum element in an array is {maximum_element}")
