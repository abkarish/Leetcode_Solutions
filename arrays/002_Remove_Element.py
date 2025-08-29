# https://leetcode.com/problems/remove-element/
# Difficulty : Easy

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        for right in range(0,len(nums)):
            if nums[right] != val:
                nums[left] = nums[right]
                left +=1
                right +=1
            else:
                right +=1
        return left