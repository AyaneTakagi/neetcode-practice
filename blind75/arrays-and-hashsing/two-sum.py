class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:

        num_dict = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[nums[i]] = i

        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

# Test code
if __name__ == "__main__":
    sol = Solution()
    print(sol.two_sum([3, 4, 5, 6], 7))  # → [0, 1]
