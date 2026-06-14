class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums = sorted(nums)

        for i in range(len(nums)):
            target = -nums[i]
            head = len(nums) - 1
            tail = 0

            while head > tail:
                cur_sum = nums[head] + nums[tail]
                if cur_sum > target or head == i:
                    head -= 1
                    continue
                if cur_sum < target or tail == i:
                    tail += 1
                    continue
                if cur_sum == target:
                    res = [nums[i], nums[head], nums[tail]]
                    if sorted(res) not in triplets:
                        triplets.append(sorted(res))
                    head -= 1
                    tail += 1

        return triplets
                