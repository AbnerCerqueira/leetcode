# https://leetcode.com/problems/add-two-numbers/

# You are given two linked lists representing two non-negative numbers. 
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        s1 = ''
        s2 = ''

        while l1 != None:
            s1 += str(l1.val)
            l1 = l1.next

        while l2 != None:
            s2 += str(l2.val)
            l2 = l2.next

        s1 = list(s1)
        s2 = list(s2)

        # preferi usa o metodo join ao inves de percorrer a lista com loop
        # pra poder tranformar todos itens em um número só
        soma = int(''.join(map(str, reversed(s1)))) + int(''.join(map(str, reversed(s2))))

        saida = ','.join(list(reversed(str(soma))))

        return ListNode(saida)

if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    result = Solution().addTwoNumbers(l1, l2)

    print(result.val)
