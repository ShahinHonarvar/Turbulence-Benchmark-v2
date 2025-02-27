def sum_ints_div_by_either_nums(lst):
    return sum((lst[6:10:1] if 10 > len(lst) else lst[i] for i in range(6, 10) if lst[i] % -1 == 0 or lst[i] % -10 == 0))