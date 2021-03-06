# 猜数字大小 II
# medium
'''
我们正在玩一个猜数游戏，游戏规则如下：

我从 1 到 n 之间选择一个数字，你来猜我选了哪个数字。

每次你猜错了，我都会告诉你，我选的数字比你的大了或者小了。

然而，当你猜了数字 x 并且猜错了的时候，你需要支付金额为 x 的现金。直到你猜到我选的数字，你才算赢得了这个游戏。

示例:

n = 10, 我选择了8.

第一轮: 你猜我选择的数字是5，我会告诉你，我的数字更大一些，然后你需要支付5块。
第二轮: 你猜是7，我告诉你，我的数字更大一些，你支付7块。
第三轮: 你猜是9，我告诉你，我的数字更小一些，你支付9块。

游戏结束。8 就是我选的数字。

你最终要支付 5 + 7 + 9 = 21 块钱。
给定 n ≥ 1，计算你至少需要拥有多少现金才能确保你能赢得这个游戏。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/guess-number-higher-or-lower-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

-------------------------------------------
题解：动态规划
本地的动态规划思路是典型的优化暴力的思路，怎么才能最少钱，单纯2分法是不知道的，所以只能暴力枚举了，
因为是看至少要准备多少钱，所以要以最坏的情况来算，就是我每次都没有选中，然后在得出来的结果集中选择花钱最少的（因为选择策略不同，会有花钱不同）

比如 n = 10, 我第一次选 1，花了 1块钱，剩下的 9 个数分别得怎么选择，是个递归问题
即 pick(1,10){i|1->n} = min(i + max(pick(1, i-1), pick(i+1, 10)))
解释，公式中 i 是第一次选择的数，按最坏情况算，因为没选中，所以得交 i 块钱，然后剩下的两段数中再分别计算需要多钱，然后取最大值，因为最坏情况
然后 10 个结果集中，选择最小的，因为题意就是最少准备

然后怎么dp，pick 函数得出来的结果，其实可以存在一个地方，给更宽的 pick 计算使用。
dp 怎么转移，其实和上面的公式一样，只不过不用再计算一遍pick了，直接从dp表里取就可以，
初始 dp[i][i] = 0，比如 dp[1][1] 意思是 pick(1,1) 从 [1] 里取一个数，那就是选择 1 直接选中了，不花钱

'''


class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * n for _ in range(n)]
        for i in range(1, n):
            for j in range(i, n):
                start = j - i
                end = j
                for k in range(start, end):
                    a = dp[start][k - 1] if k - 1 >= start else 0
                    b = dp[k + 1][end] if k + 1 <= end else 0
                    tmp = k + 1 + max(a, b)
                    dp[start][end] = min(tmp, dp[start][end] or float('inf') )
        return dp[0][-1]


print(Solution().getMoneyAmount(10))



