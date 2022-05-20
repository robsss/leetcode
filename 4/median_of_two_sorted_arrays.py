# The Python have implemented sorted funtion, maybe I should not take this shortcut.


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        """
        It seems that we should first sort array,
        then find the midian of array
        """
        merged = nums1 + nums2
        mrg_srt = sorted(merged)
        if len(mrg_srt) % 2 == 0:
            median = (mrg_srt[int(len(mrg_srt)/2 - 1)] + mrg_srt[int(len(mrg_srt)/2)])/2
        else:
            print((len(mrg_srt) - 1)/2)
            median = mrg_srt[int((len(mrg_srt) - 1)/2)]
        return median

def test_1():
    sln = Solution()
    nums1 = [1,3]
    nums2 = [2]
    print(sln.findMedianSortedArrays(nums1, nums2))

def main():
    import pdb; pdb.set_trace()
    pdb.set_trace()
    test_1()

if __name__ == "__main__":
    main()