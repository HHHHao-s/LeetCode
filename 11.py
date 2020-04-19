class Solution:
    def maxArea(self, height):
        max_area = 0
        i,j = 0,len(height) - 1
        while i < j:
            if height[i] < height[j]:
                max_area = max(max_area,height[i]*(j-i))
                i += 1
            else:
                max_area = max(max_area,height[j]*(j-i))
                j -= 1
                
        return max_area
   
   
   
   
      
a = Solution()
print(a.maxArea([1,2]))

