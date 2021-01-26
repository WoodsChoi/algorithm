// 两数相除
// medium
/*
* 给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
*
* 返回被除数 dividend 除以除数 divisor 得到的商。
*
* 整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2
*
*
*
* 示例 1:
*
* 输入: dividend = 10, divisor = 3
* 输出: 3
* 解释: 10/3 = truncate(3.33333..) = truncate(3) = 3
* 示例 2:
*
* 输入: dividend = 7, divisor = -3
* 输出: -2
* 解释: 7/-3 = truncate(-2.33333..) = -2
*
*
* 提示：
*
* 被除数和除数均为 32 位有符号整数。
* 除数不为 0。
* 假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。本题中，如果除法结果溢出，则返回 231 − 1。
*
* 来源：力扣（LeetCode）
* 链接：https://leetcode-cn.com/problems/divide-two-integers
* 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*
* --------------------------------------------
* 题解：模拟
* 模拟除法的演算过程，只不过是将10进制换成2进制进行演算，需要注意临界情况，-2147483648 除 -1 为 2147483647
*
 */

package main

import "fmt"

func main() {
	fmt.Println(divide(-2147483648, 1))
}

func divide(dividend int, divisor int) int {
	minus := false
	if dividend > 0 && divisor < 0 || dividend < 0 && divisor > 0 {
		minus = true
	}
	dividend = abs(dividend, minus)
	divisor = abs(divisor, minus)
	dist := 0
	for divisor <= dividend {
		divisor = divisor << 1
		dist++
	}
	divisor = divisor >> 1
	dist--

	ans := 0
	for dist >= 0 {
		needAdd := false
		if divisor <= dividend {
			dividend -= divisor
			needAdd = true
		}
		divisor = divisor >> 1
		dist--
		ans = ans << 1
		if needAdd {
			ans += 1
		}
	}
	if minus {
		return -ans
	}
	return ans
}

func abs(val int, isMinus bool) int {
	if val < 0 {
		if val == -2147483648 && !isMinus {
			return 2147483647
		}
		return -val
	}
	return val
}
