class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        head = len(numbers) - 1
        tail = 0
        s = 4

        while head > tail:
            cur_sum = numbers[head] + numbers[tail]
            if cur_sum > target:
                head -= 1
            if cur_sum < target:
                tail += 1
            if cur_sum == target:
                return [tail+1,head+1]