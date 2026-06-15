class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        #Find sequence start
        nums = set(nums)

        max_length = 0

        for num in nums:
            if num - 1 not in nums:
                cur_length = 1
                cur_num = num
                while True:
                    cur_num = cur_num + 1
                    if cur_num in nums:
                        cur_length += 1
                    else:
                        break
                if max_length < cur_length:
                    max_length = cur_length

        return max_length  
                    
        


            
