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
