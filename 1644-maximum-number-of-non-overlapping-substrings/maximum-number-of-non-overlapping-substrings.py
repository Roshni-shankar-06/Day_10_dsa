class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        # Step 1: Record the first and last occurrence of each character
        first = {c: i for i, c in enumerate(s)}
        last = {c: i for i, c in enumerate(s)}
     
