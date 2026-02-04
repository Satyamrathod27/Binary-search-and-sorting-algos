arr = [5, 1, 2, 4, 3]

n = len(arr)

# Bubble Sort
for i in range(n - 1):              # number of passes
    for k in range(0, n - 1 - i):   # compare adjacent elements
        if arr[k] > arr[k + 1]:
            arr[k], arr[k + 1] = arr[k + 1], arr[k]

print(arr)  # [1, 2, 3, 4, 5]
