class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if sorted(s) == sorted(t):
            return True
        else:
            return False


# ----------------------------
# Test code
# ----------------------------
if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        ("racecar", "carrace", True),
        ("jar", "jam", False),
        ("listen", "silent", True),
        ("hello", "helloo", False)
    ]

    for i, (s, t, expected) in enumerate(test_cases, 1):
        result = solution.isAnagram(s, t)
        print(f"Test Case {i}: ", "Passed" if result == expected else f"Failed (Got {result})")
