class Solution:
    def addDigits(self, num: int) -> int:
        while num // 10 >=1:
            re = (num // 10) + (num %10 )
            num = re
        return num

        