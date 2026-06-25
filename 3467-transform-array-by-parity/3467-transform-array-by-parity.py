class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        # Count how many even numbers are in the array
        even_count = sum(1 for x in nums if x % 2 == 0)
        
        # Total number of odd elements
        odd_count = len(nums) - even_count
        
        # Return an array with all 0s followed by all 1s
        return [0] * even_count + [1] * odd_count