#include <vector>
#include <algorithm>
#include <iostream>
class Solution {
public:
    void merge(std::vector<int>& nums1, int m, std::vector<int>& nums2, int n) {
         for (int j = 0, i = m; j < n; j++, i++){
            nums1[i] = nums2[j];
         }
         sort(nums1.begin(), nums1.end());
    }
};

int main(){
    std::vector<int> nums1 = {1,2,3,0,0,0};
    std::vector<int> nums2 = {2, 5, 6};
    int m = 3, n = 3;
    for (int j = 0, i = m; j < n; j++, i++){
        nums1[i] = nums2[j];
    }
    sort(nums1.begin(), nums1.end());
    for(int i = 0; i < nums1.size(); i++){
        std::cout << nums1[i] << std::endl;
    }
}



