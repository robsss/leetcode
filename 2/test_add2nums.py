# orgnize it into original file


from add_two_number import Solution 

class TestSoltion():
    def test_add_two_number(self):
        sltn = Solution()

        l1 = [2,4,3]
        l2 = [5,6,4]
        assert sltn.addTwoNumbers(l1, l2) == [7,0,8]

        l1 = [9,9,9,9,9,9,9]
        l2 = [9,9,9,9]
        assert sltn.addTwoNumbers(l1, l2) == [8,9,9,9,0,0,0,1]

        l1 = [0]
        l2 = [0]
        assert sltn.addTwoNumbers(l1, l2) == [0]



    # def test_one_element():
    #     sltn = Solution()
    #     l1 = [0]
    #     l2 = [0]
    #     assert sltn.addTwoNumbers(l1, l2) == [0]

    # def test_diff_nums_element():
    #     sltn = Solution()
    #     l1 = [9,9,9,9,9,9,9]
    #     l2 = [9,9,9,9]
    #     assert sltn.addTwoNumbers(l1, l2) == [8,9,9,9,0,0,0,1]






