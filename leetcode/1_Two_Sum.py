class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        complement = {}
        for i in range(len(nums)):
            if target - nums[i] in complement:
                return (i, complement[target - nums[i]])
            else:
                complement[nums[i]] = i
