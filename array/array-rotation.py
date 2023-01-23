print("Program for array rotation")


arr = [1, 2, 3, 4, 5, 6, 7, 8]

# Approach 1


def left_rotate(arr, n, d):
    for i in range(d):
        left_rotate_by_one(arr, n)
    return arr


def left_rotate_by_one(arr, n):
    temp = arr[0]
    for i in range(n-1):
        arr[i] = arr[i+1]
    arr[n-1] = temp


result = left_rotate(arr, len(arr), 2)
print(result)


# Approach 2
arr1 = [1, 2, 3, 4, 5, 6]


def rotate_array(arr, n, d):
    temp = []
    i = 0
    while (i < d):
        temp.append(arr[i])
        i = i+1
    i = 0
    while (d < n):
        arr[i] = arr[d]
        i = i+1
        d = d+1
    arr[:] = arr[:i] + temp
    print(arr)


rotate_array(arr1, len(arr1), 2)
