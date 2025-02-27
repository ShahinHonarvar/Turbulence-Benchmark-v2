def sum_ints_div_by_either_nums(lst):
    sum_nums = 0
    for i in range(20, 36):
        if i < len(lst) and (lst[i] % -36 == 0 or lst[i] % -89 == 0):
            sum_nums += lst[i]
    return sum_nums