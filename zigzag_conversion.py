'''题目描述：
将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行Z 字形排列。

比如输入字符串为 "PAYPALISHIRING"行数为 3 时，排列如下：

P   A   H   N
A P L S I I G
Y   I   R
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。

请你实现这个将字符串进行指定行数变换的函数
'''
def zigzag_conversion(s:str,numRows:int):
    if numRows < 2: return s
    res = ["" for _ in range(numRows)]
    i, flag = 0, -1
    for c in s:
        res[i] += c
        if i == 0 or i == numRows - 1:
            flag = -flag
        i += flag
    return "".join(res)

#test
s='leetcode'
num=3
print(zigzag_conversion(s,num))