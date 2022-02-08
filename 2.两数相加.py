'''题目描述：
给你两个非空的列表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，并且每个节点只能存储一位数字
请你将两个数相加，并且以相同形式返回一个表示和的列表
你可以假设除了数字0之外，这两个数都不会以0开头。
例：
输入：l1=[2,4,3],l2=[5,6,4]
输出：[7,0,8]
解释：342+465=807
'''
def tnumSum(list1,list2):
    l = []
    n1,n2 = 0,0
    for i in list1:
        n1 = i+10*n1
    for j in list2:
        n2 = j+10*n2
    ans=n1+n2
    for k in str(ans):
        l.append(int(k))
    l.reverse()
    return(l)
#test
list1 = [2,4,3]
list2 = [5,6,4]
print(tnumSum(list1,list2))

