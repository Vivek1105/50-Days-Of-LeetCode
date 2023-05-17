# 2130. Maximum Twin Sum of a Linked List



class Solution:
  def pairSum(self, head: Optional[ListNode]) -> int:
    def reverseList(node: ListNode) -> ListNode:
      prev = None
      while node:
        next_node = node.next
        node.next = prev
        prev = node
        node = next_node
      return prev

    max_sum = 0
    slow_ptr = head
    fast_ptr = head

    # Find the midpoint of the linked list
    while fast_ptr and fast_ptr.next:
      slow_ptr = slow_ptr.next
      fast_ptr = fast_ptr.next.next

    # Reverse the second half and store the head
    reversed_second_half_head = reverseList(slow_ptr)

    # Calculate the maximum sum of pairs
    while reversed_second_half_head:
      max_sum = max(max_sum, head.val + reversed_second_half_head.val)
      head = head.next
      reversed_second_half_head = reversed_second_half_head.next

    return max_sum
