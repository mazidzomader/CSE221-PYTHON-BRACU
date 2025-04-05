n = int(input())
temp = list(map(int, input().split()))
 
max_val = float('-inf')
max_before = temp[0]
 
for i in range(1, n):
    max_val = max(max_val, max_before + temp[i] ** 2)
    max_before = max(max_before, temp[i])
 
print(max_val)