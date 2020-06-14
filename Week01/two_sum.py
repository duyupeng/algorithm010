class Solution:
    def twoSum(self, nums, target: int) :
        n=len(nums)
        for i in range(1,n):
            tmp=nums[:i]
            if target-nums[i] in tmp:
                j=tmp.index(target-nums[i])
                break
        return [j,i]