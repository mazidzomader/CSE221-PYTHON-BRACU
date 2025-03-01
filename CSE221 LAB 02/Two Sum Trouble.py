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