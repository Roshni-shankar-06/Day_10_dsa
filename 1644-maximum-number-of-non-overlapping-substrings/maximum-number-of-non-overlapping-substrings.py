class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        # Step 1: Record the first and last occurrence of each character
        first = {c: i for i, c in enumerate(s)}
        last = {c: i for i, c in enumerate(s)}
        for i, c in enumerate(s):
            if c not in first:
                first[c] = i
        first = {c: s.index(c) for c in set(s)} # Correct first index
        
        # Helper to find a valid end index for an interval starting at 'start'
     
        
  
