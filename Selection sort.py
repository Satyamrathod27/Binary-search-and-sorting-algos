arr = [5, 1, 2, 4, 3]
n = len(arr)

# Selection Sort
for i in range(n):
    for k in range(i + 1, n):
        if arr[k] < arr[i]:
            arr[k], arr[i] = arr[i], arr[k]

print(arr)  # [1, 2, 3, 4, 5]

# for decending order
nums = [5,7,8,4,1,6,9,2]

n = len(nums)
for i in range(0,n):
   maxi = i
   for j in range(i+1,n):
       if nums[maxi]<nums[j]:
           maxi = j
   nums[i],nums[maxi]=nums[maxi],nums[i]

print(nums)

