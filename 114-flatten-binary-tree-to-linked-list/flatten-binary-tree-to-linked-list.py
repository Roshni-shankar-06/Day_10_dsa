class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        curr = root
        while curr:
            if curr.left:
                # Find the rightmost node of the left subtree
                prev = curr.left
                while prev.right:
                    prev = prev.right
                
                # Rewire the connections
                prev.right = curr.right
                curr.right = curr.left
                curr.left = None
            
            # Move to the next node on the right
            curr = curr.right
