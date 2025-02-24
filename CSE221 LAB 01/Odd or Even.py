no_of_input = int(input())
for index in range(no_of_input):
    input_per_loop = int(input())
    if (input_per_loop % 2 == 0) :
        print(f"{input_per_loop} is an Even number.")
    else :
        print(f"{input_per_loop} is an Odd number.")