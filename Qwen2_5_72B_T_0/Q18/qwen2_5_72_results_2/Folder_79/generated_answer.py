def sum_ints_div_by_either_nums(lst):
    sum_nums = 0
    for i in range(8, 10):
        if i < len(lst) and (lst[i] % -3 == 0 or lst[i] % 6 == 0):
            sum_nums += lst[i]
    return sum_nums