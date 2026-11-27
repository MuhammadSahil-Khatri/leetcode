class Solution {
public:
    set<vector<int>> s;
    void solve(vector<int>& candidates, int target, int idx,
               vector<vector<int>>& ans, vector<int>& current) {
        if (idx == candidates.size() || target < 0) {
            return;
        }

        if (target == 0) {
            if (s.find(current) == s.end()) {
                ans.push_back({current});
                s.insert(current);
            }
            return;
        }

        current.push_back(candidates[idx]);
        solve(candidates, target - candidates[idx], idx + 1, ans, current);
        solve(candidates, target - candidates[idx], idx, ans, current);

        current.pop_back();
        solve(candidates, target, idx + 1, ans, current);
    }
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> ans;
        vector<int> current;

        solve(candidates, target, 0, ans, current);

        return ans;
    }
};