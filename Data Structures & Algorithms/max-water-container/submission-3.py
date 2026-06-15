class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_w = 0
        head = len(heights) - 1 
        tail = 0 
        while head > tail:
            cur_w = min(heights[head], heights[tail]) * (head - tail)
            if cur_w > max_w: 
                max_w = cur_w
            if heights[head] > heights[tail]:
                tail += 1
            else:
                head -= 1
        
        return max_w
