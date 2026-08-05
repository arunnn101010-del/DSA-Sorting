# Promblem - kth largest element in a array 
# Approach - heap sort
# Time and space complexity - 0(n log k) & 0(k) 
# Leetcode and diffculty level - 215 & medium 
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int, vector<int>, greater<int>> pq;

        for(int num : nums) {
            pq.push(num);

            if(pq.size() > k) {
                pq.pop();

            }
        }
        return pq.top();
    }
};
