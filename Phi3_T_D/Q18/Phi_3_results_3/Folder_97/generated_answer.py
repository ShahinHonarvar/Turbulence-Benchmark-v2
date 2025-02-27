def sum_ints_div_by_either_nums(lst):
    total_sum = 0
    for i in range(58, 76):
        if lst[i] % 72 == 0 or lst[i] % 62 == 0:
            total_sum += lst[i]
    return total_sum