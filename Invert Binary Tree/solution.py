def solution(root):
    '''
        recursively swap left and right child    
    '''
    if not root:
        return
    root.right,root.left = root.left,root.right
    solution(root.left)
    solution(root.right)
    return root
    # total time N
    # total space 1