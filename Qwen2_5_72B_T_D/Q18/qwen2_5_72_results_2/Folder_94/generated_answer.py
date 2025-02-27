def sum_ints_div_by_either_nums(lst):
    sum_ = 0
    for i in range(93, 95):
        if i < len(lst) and (lst[i] % -53 == 0 or lst[i] % -91 == 0):
            sum_ += lst[i]
    return sum_