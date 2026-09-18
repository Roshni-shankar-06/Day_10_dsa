class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        
        def dfs(node, current_sum, path):
            if not node:
                return
            
            # Include the current node in the path
            path.append(node.val)
            
            # Check if it's a leaf node and the path sum matches targetSum
            if not node.left and not node.right and current_sum == node.val:
                result.append(list(path)) # Append a copy of the path
            else:
                # Continue exploring left and right subtrees
                dfs(node.left, current_sum - node.val, path)
                dfs(node.right, current_sum - node.val, path)
            
            # Backtrack: remove the current node before moving up the tree
            path.pop()
            
        dfs(root, targetSum, [])
        return result
           
