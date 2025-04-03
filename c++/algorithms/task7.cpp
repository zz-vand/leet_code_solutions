#include <vector>

class Solution {
public:
    int maxProfit(std::vector<int>& prices) {
        int mx = 0;
        for (int i = 1; i < prices.size(); i++){
            if (prices[i] > prices[i-1]){
                mx += prices[i] - prices[i-1];
            }
        }
        return mx;
    }
};