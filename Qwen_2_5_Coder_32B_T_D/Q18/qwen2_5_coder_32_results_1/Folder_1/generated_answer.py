def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in range(10, 29):
        if i < len(lst) and (lst[i] % -61 == 0 or lst[i] % -64 == 0):
            total += lst[i]
    return total