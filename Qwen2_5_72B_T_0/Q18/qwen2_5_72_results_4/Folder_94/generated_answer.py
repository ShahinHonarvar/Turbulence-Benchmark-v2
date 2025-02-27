def sum_ints_div_by_either_nums(lst):
    sum_nums = 0
    for i in range(93, 95):
        if lst[i] % -53 == 0 or lst[i] % -91 == 0:
            sum_nums += lst[i]
    return sum_nums