'''题目描述：
给你一个字符串s和一个字符规律p，请你来实现一个支持 '.'和'*'的正则表达式匹配。
'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖整个字符串s的，而不是部分字符串。
'''

def isMatch(s: str, p: str):
    # dp[i][j]代表s中的前i个字符能否用p中的前j个字符进行匹配
    if not p: return not s
    if not s and len(p) == 1: return False

    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    dp[0][0] = True
    for i in range(1, len(p) + 1):
        if p[i - 1] == '*':
            dp[0][i] = dp[0][i - 2]

    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            # 如果相等或者p为.匹配任意字母
            if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                if s[i - 1] != p[j - 2] and p[j - 2] != '.':
                    dp[i][j] = dp[i][j - 2]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 2]
    return dp[-1][-1]