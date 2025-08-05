from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        maxArea = tempArea = 0
        while left != right:
            tempArea = (right - left) * min(height[left], height[right])
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            maxArea = max(maxArea, tempArea)
        return maxArea


s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))