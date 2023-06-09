Problem - 662. Maximum Width of Binary Tree



class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque([(root, 0)])
        max_width = 0
        
        while queue:
            level_size = len(queue)
            level_width = 0
            for i in range(level_size):
                node, pos = queue.popleft()
                if node.left:
                    queue.append((node.left, 2 * pos))
                if node.right:
                    queue.append((node.right, 2 * pos + 1))
                if i == 0:
                    leftmost_pos = pos
                if i == level_size - 1:
                    rightmost_pos = pos
            level_width = rightmost_pos - leftmost_pos + 1
            max_width = max(max_width, level_width)
        
        return max_width


