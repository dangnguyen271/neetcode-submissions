class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        total_prod = 1
        for num in nums:
            total_prod *= num

        for i in range(len(nums)):
            if nums[i] != 0:
                output.append(int(total_prod / nums[i]))
            else:
                output.append(total_prod)

        return output