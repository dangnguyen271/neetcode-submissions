class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_w = 0
        for i in range(len(heights)):
            for j in range(i, len(heights)):
                cur_w = min(heights[i], heights[j]) * (j - i)
                if cur_w > max_w:
                    max_w = cur_w
                    print(i, j)
        
        return max_w
