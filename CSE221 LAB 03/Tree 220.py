def postorder_traversal(inord, preord):
    if inord == [] or preord == []:
        return []
    root = preord[0]
    root_idx = inord.index(root)
    left_inord = inord[:root_idx]
    right_inord = inord[root_idx+1:]
    left_preord = preord[1:1+len(left_inord)]
    right_preord = preord[1+len(left_inord):]
    left = postorder_traversal(left_inord, left_preord)
    right = postorder_traversal(right_inord, right_preord)

    arr = []
    for element in left:
        arr.append(element)
    for element in right:
        arr.append(element)
    arr.append(root)
    return arr
n = int(input())
inorder = list(map(int, input().split()))
preorder = list(map(int, input().split()))
print(*postorder_traversal(inorder, preorder))
