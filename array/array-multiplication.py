print("array multiplication divided by n")

arr = [100, 10, 5, 25, 35, 14]


def multiply_array(arr, n):
    multiply = 1
    for i in range(len(arr)):
        multiply *= arr[i]
    return multiply % n


result = multiply_array(arr, 11)
print(result)
