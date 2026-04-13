class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        nums = len(candies)
        greatest = max(candies)
        result = []# !!!!
        for i in range(nums):
            if candies[i] + extraCandies >= greatest:
                result.append(True) #Python 里的布尔值，必须是首字母大写，JSON（LeetCode 用来展示结果）会是小写
            else:
                result.append(False)
        
        return result# if  not , the output is [null]