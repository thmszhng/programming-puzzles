class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        prev_bit = None
        while n > 0:
            bit = n & 1
            if bit == prev_bit:
                return False
            prev_bit = bit
            n = n >> 1
        return True
