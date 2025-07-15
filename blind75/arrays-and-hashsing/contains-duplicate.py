from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False

        # return len(nums) != len(set(nums))

if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 3]
    result = solution.hasDuplicate(nums)
    print("Output:", result)  # Output: True