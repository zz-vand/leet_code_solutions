
#include <vector>
#include <algorithm>



class Solution {
public:
    void rotate(std::vector<int>& nums, int k) {
        for (int i = 0; i < k; i++){
            int tmp = nums[nums.size()-1];
            for (int j = 0; j < nums.size(); j++){
                int tmp1 = nums[j];
                nums[j] = tmp;
                tmp = tmp1;
            }
        }
    }
};



