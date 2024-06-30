import mean_calculate


def group_meann():
    class_list = {}
    frequency = []
    element_number = int(input("element_number= "))

    # 添加元素
    for i in range(element_number):
        left = float(input("left: "))
        right = float(input("right: "))
        frequency.append(int(input("frequency: ")))
        class_list[left] = right

    # 组边界是否相邻，若不是，取中加减
    lefts = list(class_list.keys())
    rights = list(class_list.values())
    # print(lefts, rights)

    class_boundary_need_change = 0
    if lefts[1] > rights[0]:
        class_boundary_need_change = 1

    if class_boundary_need_change:
        change_amount = (lefts[1] - rights[0])/2
        for i in range(element_number):
            lefts[i] -= change_amount
            rights[i] += change_amount

    # print(lefts, rights)
    # 求平均
    # frequency_num=0
    # mid_num=0
    # for i in range(element_number):
    #     mid = float((lefts[i] + rights[i]) /2)
    #     mid_num += mid * frequency[i]
    #     frequency_num += frequency[i]

    # # 3位有效数字
    # ans = "{:.3}".format(float(mid_num / frequency_num))
    print("=======mean=======")
    print(mean_calculate.group_mean(lefts, rights, frequency, element_number))
