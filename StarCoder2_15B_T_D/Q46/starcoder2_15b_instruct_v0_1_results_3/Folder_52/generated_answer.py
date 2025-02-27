def gcf_three_nums(lst):
    num1 = lst[19]
    num2 = lst[49]
    num3 = lst[74]
    while num1 != num2:
        if num1 > num2:
            num1 -= num2
        else:
            num2 -= num1
    gcf = num1
    while gcf % num3 != 0:
        gcf += num1
    return gcf