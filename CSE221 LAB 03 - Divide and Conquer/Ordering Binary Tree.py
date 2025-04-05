def Ordering_Binary_Tree(arr, left, right, return_list):
    if left > right:
        return
    mid = (left + right) // 2
    return_list.append(arr[mid])
    Ordering_Binary_Tree(arr, left, mid-1, return_list)
    Ordering_Binary_Tree(arr, mid + 1, right, return_list)
    return return_list
n = int(input())
arr = list(map(int, input().split()))
result = Ordering_Binary_Tree(arr, 0, n-1, [])
print(*result)
