# Problem - h-index 
# Approach - counting sort 
# Time and space complexity - 0(n log n) & 0(1) 
# Leetcode and diffculty level - 274 & medium 
class Solution {
public:
    int hIndex(vector<int>& citations) {

        sort(citations.begin(), citations.end());

        int n = citations.size();

        for(int i = 0; i < n; i++) {

            if(citations[i] >= n - i)
                return n - i;
        }

        return 0;
    }
};
