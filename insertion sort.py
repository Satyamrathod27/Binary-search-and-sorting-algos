arr = [5, 1, 2, 4, 3]

# Insertion Sort
for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1

    # Move elements greater than key one step ahead
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = key

print(arr)   # [1, 2, 3, 4, 5]
