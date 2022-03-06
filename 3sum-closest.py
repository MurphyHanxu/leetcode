'''题目描述：
给你一个长度为 n 的整数数组nums和 一个目标值target。请你从 nums 中选出三个整数，使它们的和与target最接近。
返回这三个数的和。
假定每组输入只存在恰好一个解。
'''


def sumcloest(list, target):
    '''
    双指针法，在三数之和（3sum）原本的函数上进行改进。
    '''
    list.sort()
    best = 10 ** 7
    i = 0
    for i in range(len(list) - 2):
        if i > 0 and list[i] == list[i - 1]:
            continue
        l = i + 1  # l是开始，r是结束
        r = len(list) - 1
        while l < r:
            ans = list[i] + list[l] + list[r]
            if ans == targrt:
                return ans

            if abs(ans - target) < abs(best - target):
                best = ans
            if ans > target:
                r -= 1
                while l < r and list[r] == list[r + 1]:
                    r -= 1
            else:
                l += 1
                while l < r and list[l] == list[l - 1]:
                    l += 1
    return best
