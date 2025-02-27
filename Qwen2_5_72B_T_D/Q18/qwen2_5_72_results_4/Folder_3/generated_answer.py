def sum_ints_div_by_either_nums(lst):
    sum_lst = 0
    for i in range(38, 53):
        if i < len(lst) and (lst[i] % -41 == 0 or lst[i] % -47 == 0):
            sum_lst += lst[i]
    return sum_lst