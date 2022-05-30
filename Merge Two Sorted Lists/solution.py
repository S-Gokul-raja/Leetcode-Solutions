class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def Solution1(list1, list2):
    '''
    merge logic of merge sort 
    '''
    pointer1 = list1
    pointer2 = list2
    ans = ListNode()
    pointer3 = ans
    while pointer1 and pointer2:
        if pointer1.val > pointer2.val:
            pointer3.next = ListNode(pointer1.val)
            pointer1 = pointer1.next
        else:
            pointer3.next = ListNode(pointer2.val)
            pointer2 = pointer2.next
        pointer3 = pointer3.next
    pointer3.next = pointer1 or pointer2
    return ans.next
    # total time n+m
    # total space n+m 

def Solution2(list1, list2):
    '''
        recursively merge 
    '''
    if not list1:
        return list2
    if not list2:
        return list1
    if list1.val<list2.val:
        list1.next = Solution2(list1.next,list2)
        return list1
    else:
        list2.next = Solution2(list2.next,list1)
        return list2
    # total time n+m
    # total space 1