class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1 = 0
        c2 = 0
        for x in nums1:
            if x in nums2:
                c2 += 1
        for x in nums2:
            if x in nums1:
                c1 += 1
        return [c2,c1]
