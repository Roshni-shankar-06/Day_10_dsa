class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # Step 1: Convert the linked list into an array
        values = []
        while head:
            values.append(head.val)
            head = head.next
            
        # Step 2: Recursively build the BST from the array
        def build_bst(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            
            # Choose the middle element as the root to maintain balance
            mid = (left + right) // 2
            root = TreeNode(values[mid])
            
            # Recursively build left and right subtrees
            root.left = build_bst(left, mid - 1)
            root.right = build_bst(mid + 1, right)
            
            return root
            
        return build_bst(0, len(values) - 1)
