# Why bother to establish a linked list by ourselves? 
# the list in Python itself is a linked list.
#
# Can I use unit test or shell script to test my code automatically?
# Yes, pytest and encapsulate them in class.
#

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



from unittest import result


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        input: list l1 and l2
        output: the sum of the two number as a list
        """
        # l1, l2 = self.get_input()

        # initialize carry
        carry = 0
        result = []
        for i in range(max(len(l1), len(l2))):
            if (i + 1) <= min(len(l1), len(l2)):
                sum = l1[i] + l2[i] + carry
            else:
                if len(l1) > len(l2):
                    sum = l1[i] + carry
                else:
                    sum = l2[i] + carry

            carry = sum // 10
            remn = sum%10
            result.append(remn)

            if (carry != 0) and ((i + 1) == max(len(l1), len(l2))):
                result.append(carry)
        return result


    # def get_input(self):
    #     """Get the lists of two integer."""
    #     l1 = input("l1: ")
    #     l2 = input("l2: ")

    #     # deal with incorprated user
    #     l1 = l1.strip(" []").split(",")
    #     l2 = l2.strip(" []").split(",")

    #     # convert
    #     l1 = [int(num) for num in l1]
    #     l2 = [int(num) for num in l2]
    #     return (l1, l2)


# def main():
#     solu = Solution()
#     result = solu.addTwoNumbers()
#     print(result)


# if __name__ == "__main__":
#     main()  


# Use pytest framework to test the functionality of the class and method
# which make life much more easier to avoid inputing by hand.

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


