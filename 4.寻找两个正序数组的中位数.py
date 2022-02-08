'''题目描述：
给定两个大小分别为m和n的正序（由小到大）数组nums1和nums2.请你找出并返回这两个正序数组的中位数。
'''
def f_median(l1,l2):
    l=l1+l2
    l.sort()
    s=len(l)
    if s%2==0:#新列表元素的个数为偶数
        median=(l[int(s/2)]+l[int(s/2-1)])/2
    else:
        median=l[s//2]
    return median
#test
l1=[1,2,3]
l2=[5,4]
print(f_median(l1,l2))