class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1 = len(word1)
        len2 = len(word2)
        i = 0
        j = 0
        merged = []
        while i < len1 or j < len2:
            if i <len1:
                merged += word[i]
                i += 1
            if j < lens2:
                merged += word[j]
                j += 1

        return ''.join(merged)
        
        