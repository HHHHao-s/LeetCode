class Solution:
    def numberOfSubarrays(self,nums, k):
        j = 0# 指针 
        list1 = []# 存放奇数位置
        result = 0# 结果
        for i,each in enumerate(nums):
            if each % 2 != 0:
                list1.append(i)
                if len(list1) > k:
                    j = list1.pop(0) + 1
            if  len(list1) == k:# 到条件成立为止的奇数组个数
                    result += list1[0] - j + 1
        return result