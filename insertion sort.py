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

nums = [3,5,6,4,8,9,10,7,1,2]
n = len(nums)
for i in range(1,n):
   key = nums[i]
   j = i-1
   while j>=0 and nums[j]>key:
       nums[j+1]=nums[j]
       j-=1
   nums[j+1]= key

print(nums)
