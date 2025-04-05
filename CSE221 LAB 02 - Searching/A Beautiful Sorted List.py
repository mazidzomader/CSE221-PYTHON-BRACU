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
