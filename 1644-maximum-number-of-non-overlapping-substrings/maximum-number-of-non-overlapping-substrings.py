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
        def check_valid_substring(start):
            end = last[s[start]]
            i = start
            while i <= end:
                # If a character inside has an earlier start, this interval is invalid
                if first[s[i]] < start:
                    return -1
                # Expand the end boundary to include all occurrences of the inner character
                end = max(end, last[s[i]])
                i += 1
            return end

        # Step 2: Generate all valid candidate intervals
        intervals = []
        for c in set(s):
            start = first[c]
            end = check_valid_substring(start)
            if end != -1:
                intervals.append((start, end))
                
        # Step 3: Sort intervals by their end index (Greedy Interval Scheduling)
        intervals.sort(key=lambda x: x[1])
        
  
