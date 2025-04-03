class Solution:
    def trap(self, height: list[int]) -> int:
        sm = 1
        for i in range(len(height)-1):
            if height[i] > height[i+1]:
                sm += 1
        if sm == len(height):
            return 0


        rain = 0

        i = 0

        while i < len(height):

            f = 0
            tmp = height[i]
            tmp_rain = 0

            for j in range(i + 1, len(height)):
                if height[j] < tmp:
                    tmp_rain += tmp - height[j]
                else:
                    f = 1
                    rain += tmp_rain
                    tmp_rain = 0
                    i = j - 1
                    break
            if f == 0:
                if i != len(height)-1:
                    height[i] = height[i]-1
                    i -= 1
            i += 1
        return(rain)