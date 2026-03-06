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

nums = [5,7,3,2,6,1,5,9]
target = 3
low = 0
high = len(nums)-1
nums.sort()

def binary(num,l,h):
   if low>high:
       return -1
   m = (l + h) // 2
   if num[m] == target:
       return nums[m]
   elif nums[m]<target:
       return binary(num,m+1,h)
   else:
       return binary(num,l,m-1)

e= binary(nums,low,high)
print(e)

# lower bound
n = len(nums)
lb=-1
while low<=high:
   mid = (low+high)//2
   if nums[mid]>=target:
       lb = mid
       high = mid-1
   else:
       low = mid+1

print(lb)

# upper bound
low  = 0
high = n-1
ub = n
target = 1
while low<=high:
   mid = (low+high)//2
   if nums[mid]>target:
       ub = mid
       high = mid-1
   else:
       low = mid+1

print(ub)

print(lb)


