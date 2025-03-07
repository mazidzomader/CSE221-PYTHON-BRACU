# A-Two Sum Trouble
m = list(map(int, input().split()))
y = list(map(int, input().split()))
target, pointer_1, pointer_2, flag = m[1], 0, m[0]-1, False
while (pointer_1 < pointer_2):
    if (y[pointer_1]+y[pointer_2] == target):
        print(f"{pointer_1+1} {pointer_2+1}")
        flag = True
        break
    elif (y[pointer_1]+y[pointer_2] < target):
        pointer_1 += 1
    else :
        pointer_2 -= 1
if flag == False :
    print(-1)

# B - beautiful sorted
len_1 = int(input())
arr1 = list(map(int, input().split()))
len_2 = int(input())
arr2 = list(map(int, input().split()))
index_1, index_2, output_arr, out_idx = 0, 0, [0]*(len_1+len_2), 0
while (index_1 < len_1 and index_2 < len_2) :
    if arr1[index_1] < arr2[index_2] :
        output_arr[out_idx] = arr1[index_1]
        index_1 += 1
    else :
        output_arr[out_idx] = arr2[index_2]
        index_2 += 1
    out_idx += 1
if (index_1<len_1):
    while (index_1 < len_1) :
        output_arr[out_idx]=arr1[index_1]
        index_1, out_idx = index_1+1, out_idx+1
if (index_2<len_2):
    while (index_2<len_2):
        output_arr[out_idx] = arr2[index_2]
        index_2, out_idx = index_2 +1, out_idx+1
print(*output_arr)

# C-longest subarray
N, K = map(int, input().split())
arr = list(map(int, input().split()))
left, sum, sub_arr_len = 0, 0, 0
 
for index in range(N):  
    sum += arr[index]
 
    while sum > K:  
        sum -= arr[left]
        left += 1  
 
    sub_arr_len = max(sub_arr_len, index - left + 1) 
print(sub_arr_len)

# D-Can you iterate
def binary_search(str, left, right):
    if left > right:
        return -1
    mid = (left+right)//2
    if (str[mid] == "1"):
      x = binary_search(str, left, mid-1) 
      if x != -1 :
          return x
      return mid+1
    else:
        return binary_search(str, mid+1, right)
           
num = int(input())
for i in range(num):
    inp = input()
    print(binary_search(inp, 0, len(inp)-1))

# E- Count the Numbers
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
