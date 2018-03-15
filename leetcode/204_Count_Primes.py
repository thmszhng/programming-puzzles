class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        
        is_prime = [True] * (n + 1)
        is_prime[0] = False
        is_prime[1] = False
        
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * 2, n + 1, i):
                    is_prime[j] = False
                    
        return sum(is_prime[:n])
