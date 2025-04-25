class The_King_of_Konigsberg():
    def __init__(self, n):
        self.board_size = n
        self.king_place = (None, None)
    def place_of_the_king(self, row, col):
        self.king_place = (row-1, col-1)
    def valid_king_direction(self):
        temp = []
        row = self.king_place[0]
        col = self.king_place[1]
        temp.append((row-1, col-1))
        temp.append((row-1, col))
        temp.append((row-1, col+1))
        temp.append((row, col-1))
        temp.append((row, col+1))
        temp.append((row+1, col-1))
        temp.append((row+1, col))
        temp.append((row+1, col+1))
        valid = []
        for i in range(len(temp)):
            if (temp[i][0]>= 0  and temp[i][0] < self.board_size) and (temp[i][1]>= 0 and temp[i][1] < self.board_size):
                valid.append((temp[i][0]+1, temp[i][1]+1))
        n = len(valid)
        print(n)
        for i in valid:
            print(*i)
            
n, position = int(input()), tuple(map(int, input().split()))

obj = The_King_of_Konigsberg(n)
obj.place_of_the_king(position[0], position[1])
obj.valid_king_direction()
