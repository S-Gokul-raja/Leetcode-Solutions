def solution(s):
    '''
    using stack 
    to push opening braces 
    and pop opening braces when correct closing braces 
    and check if stack empty 
    '''
    stack = []
    opening = {'(','{','['}
    for b in s:
        if b in opening:
            stack.append(b)
        elif stack:
            if (b == ')' and stack[-1] == '(') or \
                (b == '}' and stack[-1] == '{') or \
                (b == ']' and stack[-1] == '['):
                stack.pop() 
            else: 
                return False  
        else:
            return False
    return not stack
    # total time n
    # total space n