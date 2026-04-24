class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        
        while n % 5 == 0: #这里用 n //= 5是因为如果小于5或者3了，可以取整数而非小数
            n /= 5
        while n % 3 == 0:
            n /= 3
        return int(n) & int(n - 1) == 0

        
        