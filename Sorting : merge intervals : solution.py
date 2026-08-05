# Promblem - merge intervals 
# Approach - merge sort
# Time and space complexity - 0(n log n) & 0(n) 
# Leetcode and diffculty level - 56 & medium 
class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        vector<vector<int>>ans;

        sort(intervals.begin(), intervals.end());

        ans.push_back(intervals[0]);

        for(int i = 1; i < intervals.size(); i++) {
            if(intervals[i][0] <= ans.back()[1]) {
                ans.back()[1] = max(ans.back()[1], intervals[i][1]);
            } else {
                ans.push_back(intervals[i]);
            }
        }
        return ans;
    }
};
