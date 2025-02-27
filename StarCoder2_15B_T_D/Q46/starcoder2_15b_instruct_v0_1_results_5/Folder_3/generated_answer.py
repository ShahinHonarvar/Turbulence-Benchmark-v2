def gcf_three_nums(lst):
    num1 = lst[31]
    num2 = lst[69]
    num3 = lst[40]
    gcf = num1
    while not (gcf == num2 or gcf == num3):
        gcf -= 1
    return gcf