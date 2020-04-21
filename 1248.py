class Solution:
    def numberOfSubarrays(self,nums, k):
        m = 0# 奇数个数
        j = l = 0# 指针 
        list1 = []# 存放奇数位置
        result = 0# 结果
        for i,each in enumerate(nums):
            if each % 2 != 0 and m <= k:
                list1.append(i)
                if m + 1 > k:
                    j = l = list1.pop(0) + 1
                    m -= 1
                m += 1
            if  m == k:# 到条件成立为止的奇数组个数
                while j <= list1[0]:
                    j += 1
                    result += 1
                j = l
                

        return result

solution = Solution()
print(solution.numberOfSubarrays(nums = [2,4,6], k = 1))          
                
                
                