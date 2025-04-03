num = 1994

snum = str(num)

answer = ""

con = 4 - len(snum)

for i in range(con, len(snum)+con):
    if i == 3:
        a = int(snum[i-con])
        if a < 4 and a > 0:
            answer = answer + "I" * a
        elif a == 4:
            answer = answer + "IV"
        elif (a >= 5) and (a <= 8):
            answer = answer + "V" + "I" * (a-5)
        elif a == 9:
            answer = answer + "IX"
    if i == 2:
        a = int(snum[i-con])
        if a < 4 and a > 0:
            answer = answer + "X" * a
        elif a == 4:
            answer = answer + "XL"
        elif (a >= 5) and (a <= 8):
            answer = answer + "L" + "X" * (a-5)
        elif a == 9:
            answer = answer + "XC"
    if i == 1:
        a = int(snum[i-con])
        if a < 4 and a > 0:
            answer = answer + "C" * a
        elif a == 4:
            answer = answer + "CD"
        elif (a >= 5) and (a <= 8):
            answer = answer + "D" + "C" * (a-5)
        elif a == 9:
            answer = answer + "CM"

    if i == 0:
        a = int(snum[i-con])
        if a < 4 and a > 0:
            answer = answer + "M" * a

print(answer)