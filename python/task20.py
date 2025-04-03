class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")

        answer = ""

        for i in range(len(s)-1, -1, -1):
            if s[i] != "":
                answer = answer + s[i] + " "

        return(answer[:-1])