class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        pref = [1 for i in range(len(nums))]
        suf = [1 for i in range(len(nums))]
        
        cur_prod = 1
        for i in range(1, len(nums)):
            cur_prod *= nums[i-1]
            pref[i] = cur_prod

        cur_prod = 1
        for i in range(len(nums)-2, -1, -1):
            cur_prod *= nums[i+1]
            suf[i] = cur_prod

        for i in range(len(nums)):
            output.append(pref[i] * suf[i])

        return output