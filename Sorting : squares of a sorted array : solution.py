# Promblem - squares of a sorted array 
# Approach - two pointers 
# Time and space complexity - 0(n) & 0(n) 
# Leetcode and diffculty level - 977 & easy 
class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        int l = 0;
        int r = nums.size() - 1;
        int idx = nums.size() - 1;

        vector<int> ans(nums.size());

        while(l <= r) {

            if(abs(nums[l]) > abs(nums[r])) {
                ans[idx--] = nums[l] * nums[l];
                l++;
            }
            else {
                ans[idx--] = nums[r] * nums[r];
                r--;
            }
        }
        return ans;
    }
};
