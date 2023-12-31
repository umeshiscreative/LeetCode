### Two Sum Problem

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # for i in range(len(nums)):
        #     first = nums[i]
        #     for j in range(i+1, len(nums)):
        #         second = nums[j]
        #         if target == first + second:
        #             return [i, j]
        # return []

        newArr = nums[:]
        newArr.sort()

        start = 0
        end = len(nums) - 1
        
        while start < end:
            sum = newArr[start] + newArr[end]
            
            if sum == target:
                return [i for i,val in enumerate(nums) if val==newArr[start] or val==newArr[end]] 
            elif sum > target:
                end -= 1
            else:
                start += 1

        return []

