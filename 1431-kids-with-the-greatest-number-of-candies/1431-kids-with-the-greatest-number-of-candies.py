class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Find the maximum number of candies currently held by any kid
        max_candies = max(candies)
        
        # Check for each kid if their total after receiving extraCandies 
        # is greater than or equal to the current maximum
        return [kid_candies + extraCandies >= max_candies for kid_candies in candies]