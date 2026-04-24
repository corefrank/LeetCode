'''class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        limit = 2**31 - 1
        a= 1
        while 3 * a < limit:
            a += 1
        return n>0 and  (3* a) % n == 0
        '''

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        limit = 2**31 - 1
        x = 1
        while x * 3 <= limit:
            x *= 3
        print(x)
        return  n > 0 and x  % n == 0
        