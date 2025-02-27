def gcf_three_nums(lst):
    num1 = lst[96]
    num2 = lst[57]
    num3 = lst[85]
    gcf = min(num1, num2, num3)
    while not (num1 % gcf == 0 and num2 % gcf == 0 and (num3 % gcf == 0)):
        gcf -= 1
    return gcf