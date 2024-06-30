import group_mean
import midpoint

flag = True
while flag:
    print("=======main menu=======")
    print("1-平均；2-组中；0-退出")
    input_ = int(input("输入模式："))
    if input_ == 0:
        flag = False
    elif input_ == 1:
        group_mean.group_meann()
    elif input_ == 2:
        left = int(input("left:"))
        right = int(input("right:"))
        print("=======midpoint=======")
        print(midpoint.get_midpoint(left, right))
