class Solution:
    def hIndex(self, citations: list[int]) -> int:
        n = len(citations)
        citations.sort(reverse=True)
        print(citations)
        tmpmax = 0
        for i in range(1, n+1):
            tmp = 0
            f = 0
            for j in citations:
                if j >= i:
                    tmp += 1
                if tmp == i:
                    break
            if tmp != i:
                return i-1

            tmpmax = tmp

        return tmpmax
                