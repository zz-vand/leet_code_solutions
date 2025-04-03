class Solution:
    def romanToInt(self, s: str) -> int:
            
        roman_val = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        answer = s.count("IV")*4+s.count("IX")*9+s.count("XL")*40+s.count("XC")*90+s.count("CD")*400+s.count("CM")*900

        s = s.replace("IV", "")
        s = s.replace("IX", "")
        s = s.replace("XL", "")
        s = s.replace("XC", "")
        s = s.replace("CD", "")
        s = s.replace("CM", "")



        for i in s:
            answer += roman_val[i]

        return(answer)