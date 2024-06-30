
def group_mean(lefts,rights,frequency,elementNumber):
    frequency_num = 0
    mid_num = 0
    for i in range(elementNumber):
        mid = float((lefts[i] + rights[i]) / 2)
        mid_num += mid * frequency[i]
        frequency_num += frequency[i]

    # 3位有效数字
    ans = "{:.3}".format(float(mid_num / frequency_num))
    return ans

def mean(lst):
    # 分母
    Denominatorn = len(lst)
    # 分子
    Numerator =0
    for i in range(Denominatorn):
        Numerator += lst[i]
    return "{:.3}".format(Numerator / Denominatorn)

