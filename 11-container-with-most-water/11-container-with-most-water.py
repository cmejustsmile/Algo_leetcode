class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height)-1
        area = 0
        while i < j:
            area = max(area, (j-i)*min(height[i],height[j]))
            if height[i] < height[j]:
                i+=1
            elif height[i] > height[j]:
                j-=1
            else:
                j-=1
                i+=1
        return area