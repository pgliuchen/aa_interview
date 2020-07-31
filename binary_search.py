"""
这是一个二分查找的算法实现，请使用Python3版本以上的解释器执行
问题1：请解释一下二分查找算法
问题2：请在main入口里给这个实现加测试用例，越多越好
问题3：下面的算法有3个bug，请通过测试用例找到这3个bug并修复
"""

class Solution(object):

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        low, high = 0, len(nums) -2

        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid
            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1


if __name__ == '__main__':
    print(Solution().search([4,5,6,7,0,1,2], 4))