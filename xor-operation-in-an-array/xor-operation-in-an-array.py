class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = [0]*n
        for i in range(len(nums)):
            nums[i] = start + 2*i
        
        x = 0
        for n in nums:
            x = x^n
        return x
