'''题目描述：
给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
如果反转后整数超过 32 位的有符号整数的范围[−2**31, 2**31− 1] ，就返回 0。
假设环境不允许存储 64 位整数（有符号或无符号）。
'''
def reserve_integer(z:int):
    min = -2**31
    max = 2**31-1
    ans = 0
    while z != 0:
        if z <= min or z > max+1:
            return 0
        digit = z % 10
            # Python3 的取模运算在 x 为负数时也会返回 [0, 9) 以内的结果，因此这里需要进行特殊判断
        if z < 0 and digit > 0:
            digit -= 10
        # 同理，Python3 的整数除法在 x 为负数时会向下（更小的负数）取整，因此不能写成 x //= 10
        z = (z - digit) // 10
        ans = ans * 10 + digit
    return ans

#test
z=2**32
print(reserve_integer(z))