arr = [5, 1, 2, 4, 3]

n = len(arr)

# Bubble Sort
for i in range(n - 1):              # number of passes
    for k in range(0, n - 1 - i):   # compare adjacent elements
        if arr[k] > arr[k + 1]:
            arr[k], arr[k + 1] = arr[k + 1], arr[k]

print(arr)  # [1, 2, 3, 4, 5]

# descending bubble sort
nums = [5,7,8,4,1,9,2]

n = len(nums)

for i in range(0,n-1):
   for j in range(0,n-1-i):
       if nums[j+1]>nums[j]:
           nums[j+1],nums[j]=nums[j],nums[j+1]


print(nums)

