# 二项分布
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


def ncr(n: int, r: int) -> float:
    if r == 0:
        return 1
    up = 0
    down = 0
    down = reduce(op.mul, range(1, r + 1))
    up = reduce(op.mul, range(n, n - r, -1))
    return up / down


choices = [
    "p(X=x)",
    "p(X<x)",
    "p(X<=x)",
    "p(X>x)",
    "p(X>=x)",
    "p(a < X < b)",
    "p(a <= X <= b)",
    "mean and varience",
    "rebot",
    "quit",
]


def cal(n, p):
    choice = eg.choicebox(msg="选择要计算的", title="请问你算什么东西？", choices=choices)

    if choice == "p(X=x)":
        # r = int(input("X= "))
        r = int(eg.enterbox(msg="X=_", title="输入X=啥"))
        res = ncr(n, r) * np.power(p, r) * np.power(1 - p, n - r)
        r = f"{res}\nor\n{Fraction(res)}"
        eg.msgbox(msg=r, title="结果是")

    elif choice == "p(X<x)":
        ans = 0
        for i in range(int(eg.enterbox(msg="X<_", title="输入X<啥"))):
            ans += ncr(n, i) * np.power(p, i) * np.power(1 - p, n - i)
        r = f"{ans}\nor\n{Fraction(ans)}"
        eg.msgbox(msg=r, title="结果是")

    elif choice == "p(X>x)":
        ans = 0
        for i in range(int(eg.enterbox(msg="X>_", title="输入X>啥")) + 1, n + 1):
            # print(f"{n}C{i}({ncr(n,i)}) X {p}^{i} X {1-p}^{n-i}")
            ans += ncr(n, i) * np.power(p, i) * np.power(1 - p, n - i)
        r = f"{ans}\nor\n{Fraction(ans)}"
        eg.msgbox(msg=r, title="结果是")

    elif choice == "p(X<=x)":
        ans = 0
        for i in range(int(eg.enterbox(msg="X<=_", title="输入X<=啥")) + 1):
            ans += ncr(n, i) * np.power(p, i) * np.power(1 - p, n - i)
        r = f"{ans}\nor\n{Fraction(ans)}"
        eg.msgbox(msg=r, title="结果是")

    elif choice == "p(X>=x)":
        ans = 0
        for i in range(int(eg.enterbox(msg="X>=_", title="输入X>=啥")), n + 1):
            ans += ncr(n, i) * np.power(p, i) * np.power(1 - p, n - i)
        r = f"{ans}\nor\n{Fraction(ans)}"
        eg.msgbox(msg=r, title="结果是")

    elif choice == "p(a < X < b)":
        ans = 0
        small = 0
        rang = eg.multenterbox(msg="a < X < b", title="范围是啥", fields=["a", "b"])
        print(rang)
        for i in range(int(rang[1])):
            if i == int(rang[0]):
                small = ans  # 如果当前i为下届，则说明a<x已经算出来，保存结果
            ans += ncr(n, i) * np.power(p, i) * np.power(1 - p, n - i)
        r = f"{ans}\nor\n{Fraction(ans)}"
        eg.msgbox(msg=r, title="结果是")

    elif choice == "p(a <= X <= b)":
        ans = 0
        small = 0
        rang = eg.multenterbox(msg="a < X < b", title="范围是啥", fields=["a", "b"])
        print(rang)
        for i in range(int(rang[1]) + 1):
            if i == int(rang[0]) + 1:
                small = ans  # 如果当前i为下界+1，则说明a<=x已经算出来，保存结果
            ans += ncr(n, i) * np.power(p, i) * np.power(1 - p, n - i)
        r = f"{ans}\nor\n{Fraction(ans)}"
        eg.msgbox(msg=r, title="结果是")

    elif choice == "mean and varience":
        u = n * p  # 均值μ
        print('a')
        sig = math.sqrt(n * p * (1 - p))  # 标准差δ
        print('b')
        x = np.linspace(u - 3*sig, u + 3*sig, 100)   # 定义域
        print('c')
        y = np.exp(-(x - u) ** 2 / (2 * sig ** 2)) / (math.sqrt(2*math.pi)*sig) # 定义曲线函数
        print('d')
        plt.plot(x, y, "g", linewidth=2)    # 加载曲线
        print('e')
        plt.grid(True)  # 网格线
        print('f')
        plt.legend(labels=[f'$\mu = {u}, \sigma^2={sig ** 2}$'])
        print("g")
        plt.show()  # 显示


    elif choice == "rebot":
        return 1

    elif choice == "quit":
        sys.exit(0)


if __name__ == "__main__":
    a = ["", ""]
    while (a[0] == "") or ((a[1] == "") or ((eval(a[1]) > 1) or eval(a[1]) < 0)):
        a = eg.multenterbox(msg="n and p", fields=["n", "p"])

    n = int(a[0])
    p = float(eval(a[1]))
    while 1:
        if cal(n, p) != None:
            a = ["", ""]
            while (a[0] == "") or (
                (a[1] == "") or ((eval(a[1]) > 1) or eval(a[1]) < 0)
            ):
                a = eg.multenterbox(msg="n and p", fields=["n", "p"])
                n = int(a[0])
                p = float(eval(a[1]))
        print(n, p)
