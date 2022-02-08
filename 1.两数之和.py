'''题目描述：
给定一个整数数组nums和一个整数目标值target，请你在该数组中找出和为目标值target的那两个整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案。
'''
def twoSum(nums,target):
    lens=len(nums)
    j=-1
    for i in range(lens):
        if (target-nums[i]) in nums:
            if (nums.count(target-nums[i])==1&(target-nums[i]==nums[i])):#如果num1=num2，且nums中只出现了一次num1
                continue
            else:
                j=nums.index(target-nums[i],j+1)#index(x,j+1)是从num1后的序列找num2
                break
    if j>0:
        return[i,nums[i],j,nums[j]]
    else:
        return[]
#test
a=[1,2,3,4,6,8,9,10,12,16]
b=18
print(twoSum(a,b))