class Solution:
    def maxArea(self, height: List[int]) -> int:
         left = 0
         right = len(height)-1
         container = 0
         while left < right:
            container = max(container, min(height[left], height[right]) * (right - left)) #lower of the two heights times the distance to the right pole
            if height[left] < height[right]:
                left+=1
            else: 
                right-=1
         return container