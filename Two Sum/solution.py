def Solution1(nums,target):
    '''
    brute force:
        two loops to get all pairs to form the sum
    '''
    l = len(nums)
    for i in range(l):
        for j in range(i+1,l):
            if nums[i]+nums[j] == target:
                return [i,j]
    #total time n^2
    #total space 1

def Solution2(nums,target):
    '''
        Sorting and then using two pointer to find the sum
        Storing the index before sorting as the result needed the index and not the elements
    '''
    Dict = {}
    l = len(nums)
    for i in range(l):
        if nums[i] not in Dict:
            Dict[nums[i]] = [i]
        else:
            Dict[nums[i]]+=[i]
    # time n
    # space n
    nums.sort()
    # time n*log(n)
    start = 0
    end = l-1
    while(start<end):
        Sum = nums[start]+nums[end]
        if(Sum < target):
            start+=1
        elif(Sum > target):
            end-=1
        else:
            i1 = Dict[nums[start]][0]
            Dict[nums[start]] = Dict[nums[start]][1:]
            return [i1,Dict[nums[end]][0]]
    # time n
    # total time n + (n* log(n)) + n
    # total space n

def Solution3(nums, target):
    '''
    Storing the needed part and its index to form the sum and checking as we traverse
    '''
    Dict = {}
    l = len(nums)
    for i in range(l):
        prev = target - nums[i]
        if (prev in Dict):
            return [Dict[prev],i]
        Dict[nums[i]] = i
    # total time n
    # total space n