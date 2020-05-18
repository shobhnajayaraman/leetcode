class Solution:
    def removeVowels(self, S: str) -> str:
        vowels = ('a', 'e', 'i', 'o', 'u')
        for x in S.lower(): 
            if x in vowels:
                S = S.replace(x,"")
        return S