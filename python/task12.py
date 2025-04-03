class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        for i in range(len(gas)):
            if gas[i] < cost[i]:
                continue
            else:
                f = 0
                cost_tmp = 0
                for j in range(i, i + len(gas)):
                    if j > len(gas)-1:
                        cost_tmp += gas[j-len(gas)]-cost[j-len(gas)]
                    else:
                        cost_tmp += gas[j] - cost[j]
                    if cost_tmp < 0:
                        f = 1
                        break
                if f == 0:
                    return i

        return -1


