class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]  # The input list of sorted numbers
        :type target: int  # The target number to find or insert
        :rtype: int  # Returns the index where the target is found or should be inserted
        """
        l = 0  # Left pointer at the start of the list
        r = len(nums) - 1  # Right pointer at the end of the list
        
        while l <= r:  # Continue searching while left index is less than or equal to right index
            mid = (l + r) // 2  # Calculate the middle index
            
            if nums[mid] < target:  
                # If the middle element is smaller than the target, move the left pointer to mid + 1
                l = mid + 1  
            elif nums[mid] > target:  
                # If the middle element is larger than the target, move the right pointer to mid - 1
                r = mid - 1
            else:
                # If the middle element matches the target, return the index
                return mid  
        
        # If the target is not found, return the index where it should be inserted
        return l  
