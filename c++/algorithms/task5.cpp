#include <vector>
#include <algorithm>


class Solution {
public:
    int majorityElement(std::vector<int>& nums) {
        std::vector<int> elements;
        for (int i = 0; i < nums.size(); i++){
            if (std::find(elements.begin(), elements.end(), nums[i]) != elements.end()){
                int c = 0;
                for (int j = 0; j < nums.size(); j++){
                    if (nums[j] == nums[i]){
                        c += 1;
                    }
                }
                if (c >= nums.size()){
                    return nums[i];
                }
                elements.push_back(nums[i]);
            }
        }
    }
};