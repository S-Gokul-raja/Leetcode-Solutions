import sys
def Solution1(prices):
    '''
    brute force finding all possible buy sell pair
    '''
    l = len(prices)
    maxProfit = 0
    for i in range(l):
        for j in range(i+1,l):
            profit = prices[j]-prices[i]
            maxProfit = max(maxProfit,profit)
    return maxProfit
    # total time n^2
    # total space 1

def Solution2(prices):
    '''
    keep the min value till now
    and use it find the max profit till current index
    '''
    l = len(prices)
    minPriceTilNow = sys.maxsize
    maxProfitOnSelling = 0
    for i in range(l):
        minPriceTillNow = min(prices[i],minPriceTillNow)
        maxProfitOnSelling = max(maxProfitOnSelling,prices[i]-minPriceTillNow)
    return maxProfitOnSelling
    # total time n
    # total space 1

def Solution3(prices):
    l = len(prices)
    '''
    input            1 [1,5,6, 3,5, 1,3]
    cur = cur -prev    [0,4,1,-3,2,-4,2]
    maximum subarray is the solution
    '''
    l = len(prices)
    prev = prices[0]
    curSum = 0
    maxSum = -sys.maxsize
    for i in range(l):
        curSum = max(prices[i]-prev,curSum+(prices[i]-prev))
        maxSum = max(curSum,maxSum)
        prev = prices[i]
    return maxSum
    # total time n
    # total space 1