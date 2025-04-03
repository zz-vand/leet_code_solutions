class Solution:
    def isPalindrome(self, s: str) -> bool:
        alf = "abcdefghijklmnopqrstuvwxyz0123456789"
        s = s.lower()
        word = ""
        for i in s:
            if i in alf:
                word += i
        
        f = 0
        for i in range(len(word)-1, -1, -1):
            if word[i] != word[len(word)-1-i]:
                f = 1
                return False
        
        if f == 0:
            return True