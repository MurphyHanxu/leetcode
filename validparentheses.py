'''题目描述：
给定一个只包括 '('，')'，'{'，'}'，'['，']'的字符串 s ，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
'''
def isValid(s):
    dic = {')': '(', '}': '{', ']': '['}  # 首先构建一个哈希表，用来与栈中最后一个元素比较
    seen = "([{"  # 初始化一个全部为正括号的，因为正括号是可以随便加的，不管加在哪里，都不会影响括号是否是有效的
    lenth = len(s)  # 计算字符串的长度
    res = []  # 初始化一个栈
    for i in range(lenth):  # 对全部的字符开始遍历
        if not res:  # 如果此时栈是空的，则把相应的括号压入栈中
            res.append(s[i])  # append是一个压入函数
            continue  # continue用于跳出此次循环
        if s[i] in seen:  # 如果当前索引指向的是一个正括号
            res.append(s[i])  # 则直接加入栈即可
        else:  # 否则则是一个负括号
            if dic[s[i]] == res[-1]:  # 判断负括号是否与栈中的最后一个元素是一个完整的括号
                res.pop()  # 如果是，则把它弹出
            elif dic[s[i]] in res:
                return False  # 否则说明当前的反括号没有与之对应的相邻正括号，返回FALSE
            else:
                res.append(s[i])  # 否则，将括号加入到栈中
    if not res:  # 如果res为空，表示全部括号都已经弹出
        return True  # 此时表示是有效的括号
    return False  # 不符合上述任一条件，返回FALSE
