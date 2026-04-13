class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count =0
        for i in range(len(flowerbed)):
            
            if i == 0:
                i +1 
                count += 1
        if count == n:
            return True
        else:
            return False
