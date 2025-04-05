first_line = int(input())
second_line = input().split()
for index in range(len(second_line)-1) :
    flag = False 
    for index1 in range(len(second_line)-index-1) :
        if (int(second_line[index1]) > int(second_line[index1+1])) :
            second_line[index1], second_line[index1+1] = second_line[index1+1], second_line[index1]
            flag = True 
    if not flag :
        break
print(*second_line)