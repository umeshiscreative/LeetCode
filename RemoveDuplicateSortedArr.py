class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        replace = 1

        for current in range(1, len(nums)):
            if nums[current - 1] != nums[current]:
                nums[replace] = nums[current]
                replace += 1
        return replace
