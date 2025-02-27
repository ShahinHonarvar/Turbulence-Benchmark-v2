def sum_ints_div_by_either_nums(lst):
    sum_ = 0
    for i in range(77, 88):
        if lst[i] % 23 == 0 or lst[i] % 57 == 0:
            sum_ += lst[i]
    return sum_