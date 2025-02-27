def sum_ints_div_by_either_nums(lst):
    total_sum = 0
    for i in lst[58:76]:
        if i % 72 == 0 or i % 62 == 0:
            total_sum += i
    return total_sum