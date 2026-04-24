class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = list(map(int, str(n))) 
        pro = 1
        s = 0
        for i, x in enumerate(digits):
            pro *=x
        for j,y  in enumerate(digits):
            s += y
        return pro -s
        