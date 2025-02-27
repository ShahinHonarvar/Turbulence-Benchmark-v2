def all_ints_not_div_by_num(lst):
    not_div_by_num = []
    for i in range(56, 88):
        if lst[i] % -59 != 0:
            not_div_by_num.append(lst[i])
    return not_div_by_num