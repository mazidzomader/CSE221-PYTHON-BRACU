def lower_bound(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1
    return left
    
    
def upper_bound(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return left

x = list(map(int, input().split()))
arr = list(map(int, input().split()))
len_arr, loop = x[0], x[1]
for index in range(loop):
    x = list(map(int, input().split()))
    print(upper_bound(arr,x[1])-lower_bound(arr, x[0]))