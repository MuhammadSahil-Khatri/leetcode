
class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        int n = nums.size();
        vector<vector<int>> ans;

        sort(nums.begin(), nums.end());

        for (int i = 0; i < n - 3; i++) {

            if (i > 0 && nums[i] == nums[i - 1])
                continue;

            long long minSum = (long long)nums[i] +
                               nums[i+1] + nums[i+2] + nums[i+3];

            if (minSum > target)
                break;

            long long maxSum = (long long)nums[i] +
                               nums[n-1] + nums[n-2] + nums[n-3];

            if (maxSum < target)
                continue;

            for (int j = i + 1; j < n - 2; j++) {

                if (j > i + 1 && nums[j] == nums[j - 1])
                    continue;

                minSum = (long long)nums[i] + nums[j] +
                         nums[j+1] + nums[j+2];

                if (minSum > target)
                    break;

                maxSum = (long long)nums[i] + nums[j] +
                         nums[n-1] + nums[n-2];

                if (maxSum < target)
                    continue;

                int p = j + 1;
                int q = n - 1;

                while (p < q) {

                    long long sum = (long long)nums[i] +
                                    nums[j] + nums[p] + nums[q];

                    if (sum < target) {
                        p++;
                    }
                    else if (sum > target) {
                        q--;
                    }
                    else {
                        ans.push_back({
                            nums[i], nums[j], nums[p], nums[q]
                        });

                        p++;
                        q--;

                        while (p < q && nums[p] == nums[p-1])
                            p++;

                        while (p < q && nums[q] == nums[q+1])
                            q--;
                    }
                }
            }
        }

        return ans;
    }
};
