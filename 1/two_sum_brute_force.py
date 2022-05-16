# This is the brute force version of two sum problem 
# This is also my first problem solution of Python leetcode
# Given an array of integers nums and an integer target, return indices of the two 
# numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not
# use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
 

# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?



class Solution:
    def __init__(self):
        pass
    
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # sort nums
        # nums_sorted = sorted(nums)
        
        # search brute force method
        for idx1, num1 in enumerate(nums):
            nums2 = nums
            nums2.remove(num1)
            nums2 = nums2.insert(idx1, 0)
            
            # if only one number 
            if num1 == target:
                return idx1
            
            for idx2, num2 in enumerate(nums):
                # if two number 
                if (num1 + num2) == target:
                    return [idx1, idx2]
                else:
                    continue
        
def main():
    two_sum = Solution()
    nums = input("nums: ")
    target = input("target: ")
    nums = nums.strip().strip("[]")
    nums = nums.split(",")
    nums = [float(num) for num in nums]
    target = float(target)
    result = two_sum.twoSum(nums, target)
    print(result)
    
    
if __name__ == "__main__":
    main()
    
