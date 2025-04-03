#include <vector>

class Solution {
public:
    bool canJump(std::vector<int>& nums) {
        int aim = nums.size()-1;
        for (int i = nums.size()-2; i >= 0; i--){
            if (i + nums[i] >= aim){
                aim = i;
            }
        }
        if (aim == 0){
            return true;
        }
        return false;
    }
};