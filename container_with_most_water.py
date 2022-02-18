'''题目描述：
给定一个长度为 n 的整数数组height。有n条垂线，第 i 条线的两个端点是(i, 0)和(i, height[i])。
找出其中的两条线，使得它们与x轴共同构成的容器可以容纳最多的水。
返回容器可以储存的最大水量。
说明：你不能倾斜容器。
'''
import numpy as np
def find_volumemax(l):
    length = []
    height = []
    for i in range(len(l)):#i是下标,i=0
        for j in range(i+1, len(l)):
            length.append(j-i)
            height.append(min(l[i], l[j]))
    length_arr = np.array(length)
    height_arr = np.array(height)
    square = length_arr*height_arr
    ans = max(square.tolist())
    return ans
