def solution(s,t):
    '''
    find length and character count of both s and t
    check if lengths match
    and then check if count of characters match
    '''
    sd = {}
    sl = 0
    td = {}
    tl = 0
    for char in s:
        if char in sd:
            sd[char] +=1
        else:
            sd[char] = 1
        sl+=1
    for char in t:
        if char in td:
            td[char] +=1
        else:
            td[char]=1
        tl +=1
    if(tl != sl):
        return False
    return sd == td
    # total time slength+tlength
    # total space 1 (alphabets only max 26 * 2)