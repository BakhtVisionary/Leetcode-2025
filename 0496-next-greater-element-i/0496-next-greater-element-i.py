class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_grt_num = {}

        # Compute next greater element for each number in nums2
        for i in nums2:
            while stack and i > stack[-1]:
                smaller_num = stack.pop()
                next_grt_num[smaller_num] = i
            stack.append(i)

        # Assign -1 for elements that have no greater element
        while stack:
            next_grt_num[stack.pop()] = -1

        # Collect results for nums1
        return [next_grt_num[num] for num in nums1]
