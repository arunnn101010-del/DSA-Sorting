# Promblem - third maximum number 
# Approach - sorting 
# Time and space complexity - 0(n log n) & 0(n) 
# Leetcode and diffculty level - 414 & easy 
class Solution {
public:
    int thirdMax(vector<int>& nums) {

        set<int> st;

        for(int num : nums) {
            st.insert(num);
        }   
        
        if(st.size() < 3) {
            return *st.rbegin();
        }

        auto it = st.rbegin();

        it++;
        it++;

        return *it;
    }
};
