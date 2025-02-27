def sum_ints_div_by_either_nums(lst):
    sum_ = 0
    lst_slice = lst[93:95]
    for num in lst_slice:
        if num % -53 == 0 or num % -91 == 0:
            sum_ += num
    return sum_