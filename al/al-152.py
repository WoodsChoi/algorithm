# 乘积最大子数组
'''
给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

示例 1:

输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。

示例 2:

输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。

----------------------------------------

'''


class Solution:
    def maxProduct(self, nums) -> int:
        tmp = (1,1)
        ans = None
        for i in range(0, len(nums)):
            _max = max(tmp[0] * nums[i], tmp[1]* nums[i], nums[i])
            _min = min(tmp[0] * nums[i], tmp[1]* nums[i], nums[i])
            if ans == None or _max > ans:
                ans = _max
            tmp = (_min, _max)
        return ans

solution = Solution()
# res = solution.maxProduct([2,2,-1,3,-2,4,-5,7])
res = solution.maxProduct([2,3,0,5,7])
print(res)