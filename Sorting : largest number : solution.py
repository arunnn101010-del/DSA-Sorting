# Promblem - largest number 
# Approach - custom sort 
# Time and space complexity - 0(n log n * k ) & 09n0 
# Leetcode and diffculty level - 179 & medium class Solution {
public:
    static bool cmp(string a, string b) {
        return a+b > b+a;
    }

    string largestNumber(vector<int>& nums) {
        vector<string> arr;
        for(int num : nums) {
            arr.push_back(to_string(num));
        }

        sort(arr.begin(), arr.end(), cmp);

        if(arr[0] == "0") {
            return "0";
        }
        string ans = "";

        for(string s : arr) {
            ans += s;
        }
        return ans;
    }
};
