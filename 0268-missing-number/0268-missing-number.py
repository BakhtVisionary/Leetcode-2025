class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Calculate the sum of all elements in the given list
        current_sum = sum(nums)

        # Get the length of the list (which means numbers are in range [0, n])
        n = len(nums)

        # Calculate the expected sum of numbers from 0 to n using the formula n*(n+1)//2
        intended_sum = n * (n + 1) // 2

        # The missing number is the difference between the intended sum and the actual sum
        missing_number = intended_sum - current_sum
        
        return missing_number
