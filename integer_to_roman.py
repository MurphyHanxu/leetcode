'''题目描述：
罗马数字包含以下七种字符： I， V， X， L，C，D 和 M。
字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。
通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，
所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。
这个特殊的规则只适用于以下六种情况：
I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给你一个整数，将其转为罗马数字。
1 <= num <= 3999
'''

def intto_roman(num):
    if num<1 or num>3999:
        print('请输入1 <= num <= 3999的数字')
    else:
        ge = num%10#个位数字
        #个位数字转罗马数字
        if ge == 0:
            ger = ''
        elif ge == 1:
            ger = 'I'
        elif ge == 2:
            ger = 'II'
        elif ge == 3:
            ger = 'III'
        elif ge == 4:
            ger = 'IV'
        elif ge == 5:
            ger = 'V'
        elif ge == 6:
            ger = 'VI'
        elif ge == 7:
            ger = 'VII'
        elif ge == 8:
            ger = 'VIII'
        else:
            ger = 'IX'
        shi = (num//10)%10#十位数字
        #十位数字转罗马数字
        if shi == 0:
            shir = ''
        elif shi == 1:
            shir = 'X'
        elif shi == 2:
            shir = 'XX'
        elif shi == 3:
            shir = 'XXX'
        elif shi == 4:
            shir = 'XL'
        elif shi == 5:
            shir = 'L'
        elif shi == 6:
            shir = 'LX'
        elif shi == 7:
            shir = 'LXX'
        elif shi == 8:
            shir = 'LXXX'
        else:
            shir = 'XC'
        bai = ((num//10)//10)%10#百位数字
        #百位数字转罗马数字
        if bai == 0:
            bair = ''
        elif bai == 1:
            bair = 'C'
        elif bai == 2:
            bair = 'CC'
        elif bai == 3:
            bair = 'CCC'
        elif bai == 4:
            bair = 'CD'
        elif bai == 5:
            bair = 'D'
        elif bai == 6:
            bair = 'DC'
        elif bai == 7:
            bair = 'DCC'
        elif bai == 8:
            bair = 'DCCC'
        else:
            bair = 'CM'
        qian = (((num//10)//10)//10)%10#千位数字
        if qian == 0:
            qianr = ''
        elif qian == 1:
            qianr = 'M'
        elif qian == 2:
            qianr = 'MM'
        else:
            qianr = 'MMM'
    ans = qianr+bair+shir+ger
    return ans

def intToroman(num):
    '''
    贪心算法
    '''
    nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    index = 0
    res = ''
    while index < 13:
        # 注意：这里是等于号，表示尽量使用大的"面值"
        while num >= nums[index]:
            res += romans[index]
            num -= nums[index]
        index += 1
    return res




