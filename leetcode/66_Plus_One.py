class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        remainder = 1
        i = -1
        while remainder > 0 and abs(i) <= len(digits):
            res = digits[i] + remainder
            if res == 10:
                digits[i] = 0
                remainder = 1
            else:
                digits[i] = res
                remainder = 0
            i -= 1
        if remainder == 1:
            digits.insert(0, 1)
        return digits
