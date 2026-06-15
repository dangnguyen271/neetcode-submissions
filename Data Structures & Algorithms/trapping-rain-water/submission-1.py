class Solution:
    def trap(self, height: List[int]) -> int:
        right = len(height) - 1
        left = 0
        pivot_height = 0
        trap = 0
        
        while right >= left:
            cur_height = min(height[left], height[right])
            if cur_height > pivot_height:
                pivot_height = cur_height
            
            if height[right] < height[left]:
                if height[right] < pivot_height:
                    trap += pivot_height - height[right]
                right -= 1
            else:
                if height[left] < pivot_height:
                    trap += pivot_height - height[left]
                left += 1

        return trap


