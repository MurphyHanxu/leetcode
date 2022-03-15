'''题目描述：
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
例：
输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]
'''

def rem_nthend(list, n):
    lenth = len(list)
    list.pop(lenth-n)
    return list