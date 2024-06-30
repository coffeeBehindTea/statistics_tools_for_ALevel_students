# 泊松分布
import easygui as eg
import operator as op
from functools import reduce
from fractions import Fraction
import numpy as np
import sys
import math
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')


def bso(mu: float, r: int) -> float:
    '''
    mu: μ
    r: r\n
    bso接收用于计算泊松分布P(X = x)所需的μ和r并返回float类型的结果
    '''
    return np.power(mu, r) * np.power(math.e, -mu) / math.factorial(r)

def x_small(mu: float) -> float:
    ans = 0
    for i in range(int(eg.enterbox(msg="X<_", title="输入X<啥"))):
        ans += bso(mu, i)
    return ans

def x_small_equal(mu: float) -> float:
    ans = 0
    for i in range(int(eg.enterbox(msg="X<=_", title="输入X<=啥")) + 1):
        ans += bso(mu, i)
    return ans

choices = [
    "p(X=x)",
    "p(X<x)",
    "p(X<=x)",
    "p(X>x)",
    "p(X>=x)",
    "p(a < X < b)",
    "p(a <= X <= b)",
    "rebot",
    "quit",
]


def cal(mu: float):
    choice = eg.choicebox(msg="选择要计算的", title="请问你算什么东西？", choices=choices)

    if choice == "p(X=x)":
        # r = int(input("X= "))
        r = int(eg.enterbox(msg="X=_", title="输入X=啥"))
        res = bso(mu, r)
        r = f"{res}\nor\n{Fraction(res)}"
        eg.msgbox(msg=r, title="结果是")

    elif choice == "p(X<x)":
        r = x_small(mu)
        r = f"{r}\nor\n{Fraction(r)}"
        eg.msgbox(msg=r, title="结果是")
        

    elif choice == "p(X>x)":
        ans = 1 - x_small_equal(mu)
        r = f"{ans}\nor\n{Fraction(ans)}"
        eg.msgbox(msg=r, title="结果是")


    elif choice == "p(X<=x)":
        ans = x_small_equal(mu)
        r = f"{ans}\nor\n{Fraction(ans)}"
        eg.msgbox(msg=r, title="结果是")

    elif choice == "p(X>=x)":
        ans = 1 - x_small(mu)
        r = f"{ans}\nor\n{Fraction(ans)}"
        eg.msgbox(msg=r, title="结果是")


    elif choice == "p(a < X < b)":
        ans = 0
        rang = eg.multenterbox(msg="a < X < b", title="范围是啥", fields=["a", "b"])

        for i in range(int(rang[0])+1,int(rang[1])):
            ans += bso(mu, i)

        r = f"{ans}\nor\n{Fraction(ans)}"
        eg.msgbox(msg=r, title="结果是")

    elif choice == "p(a <= X <= b)":
        ans = 0
        rang = eg.multenterbox(msg="a < X < b", title="范围是啥", fields=["a", "b"])

        for i in range(int(rang[0]),int(rang[1]) + 1):
            ans += bso(mu, i)
        
        r = f"{ans}\nor\n{Fraction(ans)}"
        eg.msgbox(msg=r, title="结果是")


    elif choice == "rebot":
        return 1

    elif choice == "quit":
        sys.exit(0)


if __name__ == "__main__":
    a = ''
    while a == '':
        a = eg.enterbox(msg="μ")

    p = float(eval(a[0]))
    while 1:
        if cal(p) != None:
            a = ''
            while a == '':
                a = eg.multenterbox(msg="μ", fields=["μ"])
            p = float(eval(a))
        print(p)
