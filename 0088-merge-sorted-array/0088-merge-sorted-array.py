class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Merges nums2 into nums1 as one sorted array in-place.
        
        nums1 has a size of m + n, with the first m elements being valid 
        and the last n elements being placeholders (0s).
        nums2 has n elements that need to be merged into nums1.
        """
        # Pointers for the last elements of nums1 and nums2
        midx = m - 1  # Last valid index in nums1 (ignoring trailing zeros)
        nidx = n - 1  # Last index in nums2
        right = m + n - 1  # Last position in nums1 to be filled

        # Start merging from the end of nums1 to avoid overwriting elements
        while nidx >= 0:  # Continue until all elements of nums2 are placed
            # If nums1 has elements left and the last valid nums1 element is larger than the last nums2 element
            if midx >= 0 and nums1[midx] > nums2[nidx]:  
                nums1[right] = nums1[midx]  # Move nums1 element to its correct position
                midx -= 1  # Move nums1 pointer left
            else:
                nums1[right] = nums2[nidx]  # Move nums2 element to its correct position
                nidx -= 1  # Move nums2 pointer left
            
            right -= 1  # Move the position pointer left
