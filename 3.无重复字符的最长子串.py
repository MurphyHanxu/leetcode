'''题目描述：
给定一个字符串s，请你找出其中不含有重复字符的最长子串的长度
例子：
输入：s=“abcabcbb”
输出：3
'''
def findsubstring(s):
    maxlen,hashmap=0,{}
    #定义窗口的首尾端（start，end），然后滑动窗口
    start=0
    for end in range(len(s)):
        #更新需要维护的变量（maxlen，hashmap），把窗口末端元素加入哈希表，使其频率+1并且更新最大长度
        hashmap[s[end]] = hashmap.get(s[end],0)+1
        if len(hashmap)==end-start+1:
            maxlen=max(maxlen,end-start+1)
        while end -start +1>len(hashmap):
            head =s[start]
            hashmap[head]-=1
            if hashmap[head]==0:
                del hashmap[head]
            start+=1
    return maxlen

#例子
s="pwwkew"
print(findsubstring(s))
