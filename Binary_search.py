def binary_search(arr, target):
    arr.sort()  # Binary search requires a sorted array
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return -1


arr = [3, 645, 342, 23, 67, 44, 11, 6, 7, 9, 1, 2, 4, 6, 7, 99]
print(binary_search(arr, 1))
