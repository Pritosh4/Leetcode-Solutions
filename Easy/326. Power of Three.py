class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        elif n % 3 == 0:
            return self.isPowerOfThree(n/3)
        elif n == 1:
            return True
        return False
        
