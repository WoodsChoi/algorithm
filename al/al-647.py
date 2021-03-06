# 回文子串
# medium
'''
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。

示例 1：

输入："abc"
输出：3
解释：三个回文子串: "a", "b", "c"

示例 2：

输入："aaa"
输出：6
解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa" 

提示：

输入的字符串长度不会超过 1000 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindromic-substrings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''


class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = len(s)
        dp = [[i] for i in range(len(s))]
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                dp[i].append(i - 1)
                ans += 1
            for index in dp[i - 1]:
                if index - 1 >= 0 and s[index - 1] == s[i]:
                    dp[i].append(index - 1)
                    ans += 1
        return ans


print(Solution().countSubstrings('aaaa'))