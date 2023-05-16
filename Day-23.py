# 24. Swap Nodes in Pairs
 


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node as the new head
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        while current.next and current.next.next:
            # Nodes to be swapped
            node1 = current.next
            node2 = current.next.next

            # Swap nodes
            node1.next = node2.next
            node2.next = node1
            current.next = node2

            # Move the pointer to the next pair
            current = current.next.next

        return dummy.next
      
