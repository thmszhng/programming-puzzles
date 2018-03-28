class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # if we only have 1 pair of increasing adjacent elemns, then to return True
        # we must be able to modify one of them to arrive at a valid non-decr list
        
        nums = [float('-inf')] + nums + [float('inf')]
        
        incr_idx = None  # idx of first elem in pair of increasing adjacent elems
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if incr_idx is not None:
                    return False  # > 1 pair of increasing adjacent elems
                incr_idx = i
        
        if incr_idx is None:
            return True
        
        return (nums[incr_idx - 1] <= nums[incr_idx + 1]) or (nums[incr_idx] <= nums[incr_idx + 2])
