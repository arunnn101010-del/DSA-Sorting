# Promblem - array partition 
# Approach - sorting 
# Time and space complexity - 0(n) & 0(1) 
# Leetcode and diffculty level - 561 & easy 
class Solution {
public:
    int arrayPairSum(vector<int>& nums) {

        sort(nums.begin(), nums.end());

        int sum = 0;

        for(int i = 0; i<nums.size(); i+=2) {
            sum += nums[i];
        }
        return sum;
    }
};

