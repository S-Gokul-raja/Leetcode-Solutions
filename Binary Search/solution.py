def solution(nums, target):
    '''
    finding mid and comparing the target
    each iteration reduces half the search space
    '''
    start = 0
    end = len(nums)-1
    while(start<=end):
        mid = start + (end-start)//2
        if(nums[mid] == target):
            return mid
        elif(nums[mid]<target):
            start = mid+1
        else:
            end = mid-1
    return -1
    # total time log(N)
    # total space 1