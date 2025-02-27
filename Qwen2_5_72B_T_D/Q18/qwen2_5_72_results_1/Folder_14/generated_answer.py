def sum_ints_div_by_either_nums(lst):
    result = 0
    for i in range(7, 10):
        if i < len(lst) and (lst[i] % 2 == 0 or lst[i] % 3 == 0):
            result += lst[i]
    return result