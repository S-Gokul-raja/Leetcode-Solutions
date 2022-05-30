def Solution(s):
    '''
    ignore non alphanumeric and check start and end 
    '''
    start = 0
    end = len(s)-1
    while start < end:
        i = s[start]
        j = s[end]
        if(not i.isalnum()):
            start+=1
            continue
        if(not j.isalnum()):
            end-=1
            continue
        if(i.lower() == j.lower()):
            start+=1
            end-=1
        else:
            return False
    return True
    # total time n
    # total space 1