import sys

def solution(nums):
    '''
    Kadane's algorithm
    '''
    curMax = 0
    ans = -sys.maxsize
    for num in nums:
        curMax = max(num,curMax+num)
        ans = max(ans,curMax)
    return ans
    # total time N
    # total space 1