// 钥匙和房间
// medium
/*
* 有 N 个房间，开始时你位于 0 号房间。每个房间有不同的号码：0，1，2，...，N-1，并且房间里可能有一些钥匙能使你进入下一个房间。
*
* 在形式上，对于每个房间 i 都有一个钥匙列表 rooms[i]，每个钥匙 rooms[i][j] 由 [0,1，...，N-1] 中的一个整数表示，其中 N = rooms.length。 钥匙 rooms[i][j] = v 可以打开编号为 v 的房间。
*
* 最初，除 0 号房间外的其余所有房间都被锁住。
*
* 你可以自由地在房间之间来回走动。
*
* 如果能进入每个房间返回 true，否则返回 false。
*
* 示例 1：
*
* 输入: [[1],[2],[3],[]]
* 输出: true
* 解释:
* 我们从 0 号房间开始，拿到钥匙 1。
* 之后我们去 1 号房间，拿到钥匙 2。
* 然后我们去 2 号房间，拿到钥匙 3。
* 最后我们去了 3 号房间。
* 由于我们能够进入每个房间，我们返回 true。
* 示例 2：
*
* 输入：[[1,3],[3,0,1],[2],[0]]
* 输出：false
* 解释：我们不能进入 2 号房间。
* 提示：
*
* 1 <= rooms.length <= 1000
* 0 <= rooms[i].length <= 1000
* 所有房间中的钥匙数量总计不超过 3000。
*
* 来源：力扣（LeetCode）
* 链接：https://leetcode-cn.com/problems/keys-and-rooms
* 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

-----------------------------------------
* 题解：dfs
* 乍一看好像跟一笔画类题(欧拉图)似的，但是每间屋打开后就是永久打开了，不需要再通过钥匙打开，可以在已打开的屋子之间来回穿噔，
* 所以就退化成了dfs

*/

package main

import "fmt"

func main() {
	para := [][]int{}
	para = append(para, []int{1, 3})
	para = append(para, []int{3, 0, 1})
	para = append(para, []int{2})
	para = append(para, []int{0})
	ret := canVisitAllRooms(para)
	fmt.Println(ret)
}

func canVisitAllRooms(rooms [][]int) bool {
	n := len(rooms)
	flag := make([]bool, n)
	var dfs func(index int)
	dfs = func(index int) {
		flag[index] = true
		for len(rooms[index]) > 0 {
			next := rooms[index][0]
			rooms[index] = rooms[index][1:]
			flag[next] = true
			dfs(next)
		}
	}
	dfs(0)
	for i := range flag {
		if flag[i] == false {
			return false
		}
	}
	return true
}
