arr = [5, 1, 2, 4, 3]
n = len(arr)

# Selection Sort
for i in range(n):
    for k in range(i + 1, n):
        if arr[k] < arr[i]:
            arr[k], arr[i] = arr[i], arr[k]

print(arr)  # [1, 2, 3, 4, 5]
