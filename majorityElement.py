#169. Majority Element
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majority = 0
        count = 0
        for n in nums:
            if count == 0:
                majority = n
