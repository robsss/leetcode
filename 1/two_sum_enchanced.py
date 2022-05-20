# Generally, sorting before searching make life much more easier.
# Therefore, sorting and comparing the target and element of nums
# counts.
# TODO: Finish this follow-up version.



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

# How can I analyze the best and worst case complexity?
# big O notation and big omega notation?


class Solution:
    def __init__(self, nums: list[int], target: int):
        self.nums = nums
        self.target = target


    def twoSum(self):
        # sort nums
        self.sort_nums()

        # get nums
        nums = self.nums
        target = self.target

        # search brute force method
        for idx1, num1 in enumerate(nums):
            # may not use the same element twice
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


    def sort_nums(self):
        """It would be better to sort the list befroe searching"""
        nums = self.nums
        target = self.target
        # sort in normal order
        nums_sorted = sorted(nums)
        for idx, num in enumerate(nums_sorted):
            # target must be added by small number
            if num > target:
                self.nums = nums_sorted[:idx]


def main():
    nums, target = get_num()
    two_sum = Solution(nums, target)
    result = two_sum.twoSum()
    print(result)


def get_num():
    nums = input("nums: ")
    target = input("target: ")
    nums = nums.strip().strip("[]")
    nums = nums.split(",")
    nums = [float(num) for num in nums]
    target = float(target)
    return (nums, target)


if __name__ == "__main__":
    main()

