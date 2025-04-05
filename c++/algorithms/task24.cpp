#include <algorithm>
#include <vector>

class Solution {
public:
    int maxArea(std::vector<int>& height) {
        
        int mx = 0;
        int left = 0;
        int right = height.size() - 1;

        while (left < right) {  
            int currentHeight = std::min(height[left], height[right]);
            int currentWidth = right - left;
            mx = std::max(currentHeight * currentWidth, mx);

            if (height[left] < height[right]) {
                left++;  
            } else {
                right--;  
            }
        }

        return mx;
    }
};