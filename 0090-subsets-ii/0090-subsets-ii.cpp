class Solution {
public:
    void subsets(vector<int>& nums, vector<int>& ans, int i,
                 vector<vector<int>>& powerSet) {
        if (i == nums.size()) {
            powerSet.push_back(ans);
            return;
        }

        ans.push_back(nums[i]);
        subsets(nums, ans, i + 1, powerSet);

        ans.pop_back();

        int idx = i + 1;
        while (idx < nums.size() && nums[idx] == nums[idx - 1])
            idx++;

        subsets(nums, ans, idx, powerSet);
    }

    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> powerSet;
        vector<int> ans;

        subsets(nums, ans, 0, powerSet);

        return powerSet;
    }
};