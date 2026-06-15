class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        total_prod = 1
        total_prod0 = 0
        for num in nums:
            total_prod *= num
            if num != 0:
                if total_prod0 == 0:
                    total_prod0 += num
                else:
                    total_prod0 *= num

        print(total_prod, total_prod0)

        for i in range(len(nums)):
            if nums[i] != 0:
                output.append(int(total_prod / nums[i]))
            else:
                output.append(total_prod0)

        return output