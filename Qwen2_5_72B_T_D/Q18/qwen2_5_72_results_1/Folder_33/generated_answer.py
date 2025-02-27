def sum_ints_div_by_either_nums(lst):
    sum_nums = 0
    for i in range(281, 695):
        if i < len(lst) and (lst[i] % -722 == 0 or lst[i] % -731 == 0):
            sum_nums += lst[i]
    return sum_nums