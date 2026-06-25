class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        # Initialize the permutation P = [1, 2, ..., m]
        P = list(range(1, m + 1))
        result = []
        
        for q in queries:
            # Find the 0-indexed position of the current query element
            idx = P.index(q)
            result.append(idx)
            
            # Remove the element from its current position and move it to the front
            P.pop(idx)
            P.insert(0, q)
            
        return result
        