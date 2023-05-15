# 1721. Swapping Nodes in a Linked List

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Initialize pointers
        first = head
        second = head

        # Move the first pointer k nodes ahead
        for _ in range(k - 1):
            first = first.next

        # Save the reference to the first node for swapping later
        node_k = first

        # Move both pointers until the first pointer reaches the end
        while first.next:
            first = first.next
            second = second.next

        # Swap the values of the kth node from the beginning and end
        node_k.val, second.val = second.val, node_k.val

        return head
