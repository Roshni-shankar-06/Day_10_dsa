class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # Step 1: Convert the linked list into an array
        values = []
        while head:
            values.append(head.val)
            head = head.next
            
        # Step 2: Recursively build the BST from the array
      
       
         
