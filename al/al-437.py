# 路径总和 III
# easy
'''
给定一个二叉树，它的每个结点都存放着一个整数值。

找出路径和等于给定数值的路径总数。

路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。

示例：

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

返回 3。和等于 8 的路径有:

1.  5 -> 3
2.  5 -> 2 -> 1
3.  -3 -> 11

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/path-sum-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''

import treeFunc

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if root == None:
            return 0
        ans = 0
        queue = [[root, 0]]
        while len(queue) > 0:
            item = queue[-1]
            node = item[0]
            if node.left and item[1] & 1 == 0 :
                item[1] |= 1
                queue.append([node.left, 0])
            elif node.right and item[1] & 2 == 0:
                item[1] |= 2
                queue.append([node.right, 0])
            else:
                _sum = 0
                for i in range(len(queue) - 1, -1, -1):
                    _sum += queue[i][0].val
                    if _sum == sum:
                        ans += 1
                queue.pop()
        return ans


print(Solution().pathSum(treeFunc.deserialize([10,5,-3,3,2,None,11,3,-2,None,1]), 8))