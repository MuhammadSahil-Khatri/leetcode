class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        unordered_map<int, int> freq;
        freq[0] = 1;

        int prefixSum = 0;
        int count = 0;

        for (int num : nums) {
            prefixSum += num;

            int val = prefixSum - k;

            if (freq.find(val) != freq.end()) {
                count += freq[val];
            }

            freq[prefixSum]++;
        }

        return count;
    }
};