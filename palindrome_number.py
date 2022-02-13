'''题目描述：
给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。例如，121 是回文，而 123 不是。
'''
from reverse_integer import*
def palindrome_number(num):
    if num<0:
        return 0
    elif num == 0:
        return 1
    else:
        if reserve_integer(num) == num:
            return 1
        else:
            return 0

