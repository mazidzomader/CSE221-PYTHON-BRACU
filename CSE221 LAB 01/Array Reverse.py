first_line = input().split()
second_line = input().split()
for index in range(int(first_line[0])//2) :
    second_line[index], second_line[len(second_line)-1-index] = second_line[len(second_line)-1-index], second_line[index]
print(*second_line[int(first_line[0])-int(first_line[1]):])