no_of_input = int(input())
for index in range(no_of_input):
    input_per_loop = input()
    input_mod = input_per_loop.split()
    if input_mod[2] == "+" :
        print(int(input_mod[1])+int(input_mod[3]))
    elif input_mod[2] == "-" :
        print(int(input_mod[1])-int(input_mod[3]))
    elif input_mod[2] == "*" :
        print(int(input_mod[1])*int(input_mod[3]))
    elif input_mod[2] == "/" :
        print(int(input_mod[1])/int(input_mod[3]))
    else :
        pass
   