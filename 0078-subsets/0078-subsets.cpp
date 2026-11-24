class Solution {
public:
    void subsets(vector<int>& nums, vector<vector<int>>& powerSet,
                 vector<int>& ans, int i) {

        if (i == nums.size()) {
            powerSet.push_back(ans);
            return;
        }

        // Include nums[i]
        ans.push_back(nums[i]);
        subsets(nums, powerSet, ans, i + 1);

        // Backtrack
        ans.pop_back();

        // Exclude nums[i]
        subsets(nums, powerSet, ans, i + 1);
    }

    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> powerSet;
        vector<int> ans;

        subsets(nums, powerSet, ans, 0);
        return powerSet;
    }
};