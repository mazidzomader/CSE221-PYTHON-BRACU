no_of_students = int(input())
student_id = input().split()
student_marks = input().split()
count = 0
for index in range(no_of_students):
    student_id[index] = int(student_id[index])
    student_marks[index]  = int(student_marks[index])

for index in range(no_of_students - 1):
    minimum_index = index
    for index1 in range(index + 1, no_of_students):
        if (student_marks[index1] == student_marks[minimum_index] and student_id[index1] < student_id[minimum_index]) or (student_marks[index1] > student_marks[minimum_index]) :
            minimum_index = index1
    if minimum_index != index:
        student_marks[index], student_marks[minimum_index] = student_marks[minimum_index], student_marks[index]
        student_id[index], student_id[minimum_index] = student_id[minimum_index], student_id[index]
        count += 1

print("Minimum swaps:", count)
for i in range(no_of_students):
    print(f"ID: {student_id[i]} Mark: {student_marks[i]}")
