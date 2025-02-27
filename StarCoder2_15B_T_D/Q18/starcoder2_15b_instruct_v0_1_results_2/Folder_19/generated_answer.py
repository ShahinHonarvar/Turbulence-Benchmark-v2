def sum_ints_div_by_either_nums(lst):
    sum_ints = 0
    for i in range(1, 5):
        if lst[i] % 4 == 0 or lst[i] % -6 == 0:
            sum_ints += lst[i]
    return sum_ints