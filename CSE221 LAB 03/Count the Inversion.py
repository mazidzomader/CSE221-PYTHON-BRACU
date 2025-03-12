def merge(a, b):
    x, y= len(a), len(b)
    arr = []
    inv, i, j = 0, 0, 0
 
    while i < x and j < y:
        if a[i] < b[j]:
            arr.append(a[i])
            i += 1
        else:
            arr.append(b[j])
            inv += (x - i)  
            j += 1
 
    while i < x:
        arr.append(a[i])
        i += 1
 
    while j < y:
        arr.append(b[j])
        j += 1
 
    return (inv, arr)
 
def mergeSort(arr):
    if len(arr) <= 1:
        return (0, arr)  
 
    mid = len(arr) // 2
    a1 = mergeSort(arr[:mid])
    a2 = mergeSort(arr[mid:])
    merged = merge(a1[1], a2[1])  
    return (merged[0] + a1[0] + a2[0], merged[1]) 
 
 
n = int(input())
arr = list(map(int, input().split()))
 
x = mergeSort(arr)
print(x[0])  
print(*x[1])