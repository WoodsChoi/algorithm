// 俄罗斯套娃信封问题
// hard
/*
* 给定一些标记了宽度和高度的信封，宽度和高度以整数对形式 (w, h) 出现。当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。
*
* 请计算最多能有多少个信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。
*
* 说明:
* 不允许旋转信封。
*
* 示例:
*
* 输入: envelopes = [[5,4],[6,4],[6,7],[2,3]]
* 输出: 3
* 解释: 最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。
*
* 来源：力扣（LeetCode）
* 链接：https://leetcode-cn.com/problems/russian-doll-envelopes
* 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*
* ----------------------------------------------------------------
* 题解：二分查找 + 动态规划(贪心)
*
* 此题整个信封又套娃的迷惑了双眼，其实如果把这些信封按 w 从小到大先排个序，然后在 h 中找最长单调递增子序列即可。
* 对！此题就是典型的 LIS 问题。
*
* 假设一个状态转移队列 f，f[i] = h 是指以当前 h 为末尾的能构成当前长度 i+1 的 LIS 的最小值，
* 当遇到某个 hj，如果它比 f[i] 大，那么 hj 可以直接加到 f 后面，构成长度 i+2 的 LIS，
* 如果 hj 比 f[i] 小，那么就从 f 里找到比 hj 大的那个元素 f[j]，将它替换成 hj，以保证到目前为止能构成长度 j+1 的 LIS 里 f[j] 是最小的。
*
* 因为要输出的是 LIS 的长度，所以始终保持 f 里每个位置的值是当前长度 LIS 里最小的就 ok，
* 无需关心 h 较后的元素把 f 里 h 较前的元素覆盖了，因为如果 h 后续的元素没能把 f 后段全替换掉，并且有新增，
* 那么 LIS 的长度还是恒定的。
*
* 最后输出 f 的长度即是答案。
*
 */

package main

import "sort"

func main() {

}

func maxEnvelopes(envelopes [][]int) int {
	sort.Slice(envelopes, func(x, y int) bool {
		a, b := envelopes[x], envelopes[y]
		return a[0] < b[0] || a[0] == b[0] && a[1] > b[1]
	})

	f := []int{}
	for _, e := range envelopes {
		h := e[1]
		if i := sort.SearchInts(f, h); i < len(f) {
			f[i] = h
		} else {
			f = append(f, h)
		}
	}
	return len(f)
}