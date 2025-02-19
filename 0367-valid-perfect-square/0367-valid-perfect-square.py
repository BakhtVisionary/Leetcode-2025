class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        """
        Determines if a given number is a perfect square using binary search.
        
        :param num: The number to check.
        :return: True if num is a perfect square, False otherwise.
        """
        l = 1  # Left boundary for binary search
        r = num  # Right boundary for binary search

        while l <= r:  # Continue until the search space is exhausted
            mid = (l + r) // 2  # Find the middle number
            square = mid * mid  # Calculate the square of mid
            
            if square == num:  # If the square matches num, it's a perfect square
                return True
            elif square < num:  # If square is smaller, search the right half
                l = mid + 1
            else:  # If square is larger, search the left half
                r = mid - 1
        
        return False  # If no perfect square is found, return False