'''题目描述：
给你一个包含 n 个整数的数组nums，判断nums中是否存在三个元素 a，b，c ，使得a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。
注意：答案中不可以包含重复的三元组。
示例 1：
输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
'''


def sum(list):
    '''双指针法'''
    list.sort()
    ans = []
    i = 0
    for i in range(len(list)-2):
        if list[i] > 0:
            break  # 因为此时三个数都为正数，必不为0
        if i > 0 and list[i] == list[i-1]:
            continue
        l = i + 1
        r = len(list) - 1
        while l < r:
            s = list[i]+list[l]+list[r]
            if s < 0:
                l += 1
                while l < r and list[l] == list[l-1]:
                    l += 1
            elif s > 0:
                r -= 1
                while l < r and list[r] == list[r+1]:
                    r -= 1
            else:
                ans.append([list[i], list[l], list[r]])
                l += 1
                r -= 1
                while l < r and list[l] == list[l - 1]: l += 1
                while l < r and list[l] == list[r + 1]: r -= 1
    return ans