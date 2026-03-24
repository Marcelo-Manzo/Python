# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 == None or l2 == None:
            print("não são aceitas listas vazias")
            return ValueError
        
        Num1 = 0
        Num2 = 0

        
        count = 0
        
        while l1:
            Num1 += l1.val*10**count
            count+=1
            l1 = l1.next

        count = 0
    
        while l2:
            Num2 += val*10**count
            count+= 1
            l2 = l2.next

        return Num1 + Num2


# 1 - 3 - 12 -----  1231 = 12 * 100 + 3 *10 + 1 *1