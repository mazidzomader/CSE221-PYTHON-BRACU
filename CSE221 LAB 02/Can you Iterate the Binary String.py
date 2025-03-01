def binary_search(str, left, right):
    if left > right:
        return -1
    mid = (left+right)//2
    if (str[mid] == "1"):
      x = binary_search(str, left, mid-1) 
      if x != -1 :
          return x
      return mid+1
    else:
        return binary_search(str, mid+1, right)
           
num = int(input())
for i in range(num):
    inp = input()
    print(binary_search(inp, 0, len(inp)-1))
