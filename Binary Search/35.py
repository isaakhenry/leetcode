import math
from typing import List


class Solution:
    def searchInsert(nums: List[int], target: int) -> int:
        lp, rp, = 0, len(nums) - 1
        while lp <= rp:
            mid = (lp + rp) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                rp = mid - 1
            else:
                lp = mid + 1
        return lp 
      

    test = [1,3,5,6]
    searchInsert(test, 2)