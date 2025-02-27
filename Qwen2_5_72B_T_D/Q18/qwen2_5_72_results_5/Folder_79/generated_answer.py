def sum_ints_div_by_either_nums(lst):
    result = 0
    for i in range(8, 10):
        if i < len(lst) and (lst[i] % -3 == 0 or lst[i] % 6 == 0):
            result += lst[i]
    return result