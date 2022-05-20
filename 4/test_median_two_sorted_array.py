from median_of_two_sorted_arrays import Solution

class TestSolution():
    def test_1(self):
        sln = Solution()
        nums1 = [1,3]
        nums2 = [2]
        assert sln.findMedianSortedArrays(nums1, nums2) == 2

    def test_2(self):
        sln = Solution()
        nums1 = [1,2]
        nums2 = [3,4]
        assert sln.findMedianSortedArrays(nums1, nums2) == 2.5