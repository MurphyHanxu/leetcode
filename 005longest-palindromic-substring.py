'''题目描述：
给你一个字符串s，找到s中最长的回文子串
'''
def f_palindrome(s):
    '''
    dp[i][j]记录s[i:j]是不是一个回文串，满足以下两个条件就是
    1.s[i]=s[j]
    2.s[i+1,j-1]是一个回文串，这里用一个条件判断i+1>=j-1,初始化长度为1和0的串为回文串'''
    length = len(s)
    dp = [[1]*length for _ in range(length)]
    left,right = 0,0
    for i in range(1,length):
        for j in range(length-i):
            if s[j]==s[j+i] and dp[j+1][j+i-1]:
                dp[j][j+1]=1
                left,right = j,j+1
            else:
                dp[j][j+1] = 0
    return s[left:right+1]

s="aba"
print(f_palindrome(s))

