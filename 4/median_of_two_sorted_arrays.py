"""
Given two sorted arrays nums1 and nums2 of size m and n respectively,
return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:
```
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
```

Example 2:
```
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
```

Constraints:

- nums1.length == m
- nums2.length == n
- 0 <= m <= 1000
- 0 <= n <= 1000
- 1 <= m + n <= 2000
- -106 <= nums1[i], nums2[i] <= 106

"""
# The Python have implemented sorted funtion, maybe I should not take
# this shortcut.


class Solution:
    """
    Encapsulate the funciton into a class
    """
    def __init__(self):
        pass


    def find_median_sorted_arrays(self, nums1: list[int],
                                        nums2: list[int]) -> float:
        """
        It seems that we should first sort array,
        then find the midian of array
        """
        merged = nums1 + nums2
        mrg_srt = sorted(merged)
        if len(mrg_srt) % 2 == 0:
            median = (mrg_srt[int(len(mrg_srt)/2 - 1)] + \
                      mrg_srt[int(len(mrg_srt)/2)])/2
        else:
            print((len(mrg_srt) - 1)/2)
            median = mrg_srt[int((len(mrg_srt) - 1)/2)]
        return median

    def sort(self):
        """sort array"""
        ...


def test_1():
    """Test"""
    sln = Solution()
    nums1 = [1,3]
    nums2 = [2]
    print(sln.find_median_sorted_arrays(nums1, nums2))


def main():
    """main func"""
    test_1()


if __name__ == "__main__":
    main()
