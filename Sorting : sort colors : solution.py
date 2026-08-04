# Promblem - sort colors 
# Approach - dutch national flag ( 3 pointers ) 
# Time and space complexity - 0(n) & 0(1) 
# Leetcode and diffculty level - 75 & easy 
class Solution {
public:
    void sortColors(vector<int>& nums) {
        int low = 0, mid = 0;
        int high = nums.size() - 1;

        while(mid <= high ) {
            if(nums[mid] == 0) {
                swap(nums[low], nums[mid]);
                low++;
                mid++;
            }
            else if(nums[mid] == 1) {
                mid++;
            }
            else {
                swap(nums[mid], nums[high]);
                high--;
            }
        }
    }
};
