def gcf_three_nums(nums_list):
    a, b, c = (nums_list[95], nums_list[56], nums_list[84])
    while b:
        a, b = (b, a % b)
    while c:
        a, c = (c, a % c)
    return a