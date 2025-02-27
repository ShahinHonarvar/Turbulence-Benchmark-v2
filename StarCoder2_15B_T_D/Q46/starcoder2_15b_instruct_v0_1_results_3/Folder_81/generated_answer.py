def gcf_three_nums(num_list):
    num20 = num_list[20]
    num17 = num_list[17]
    num28 = num_list[28]
    while num17 != 0:
        num20, num17 = (num17, num20 % num17)
    while num28 != 0:
        num17, num28 = (num28, num17 % num28)
    return num28