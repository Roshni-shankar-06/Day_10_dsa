class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        
        def dfs(node, current_sum, path):
            if not node:
                return
            
            # Include the current node in the path
            path.append(node.val)
            
           
