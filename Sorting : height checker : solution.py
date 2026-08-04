# Promblem - height checker 
# Approach - count sorting 
# Time and space complexity - 0(n log n) & 0(n) 
# Leetcode and diffculty level - 1051 & easy 
class Solution {
public:
    int heightChecker(vector<int>& heights) {

        vector<int> expected = heights;

        sort(expected.begin(),expected.end());

        int count = 0;
        for(int i=0; i<heights.size(); i++) {
            if(heights[i] != expected[i])
            count++;
        }
        return count;
    }
};
