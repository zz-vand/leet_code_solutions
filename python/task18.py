class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s1 = s.split(" ")

        for i in range(len(s1)-1, -1, -1):
            if len(s1[i]) > 0:
                return len(s1[i])