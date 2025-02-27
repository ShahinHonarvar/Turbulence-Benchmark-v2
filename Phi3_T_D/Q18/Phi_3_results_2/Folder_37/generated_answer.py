def sum_ints_div_by_either_nums(lst):
    return sum((lst[2:8][i] for i in range(len(lst[2:8])) if lst[2:8][i] % -1 == 0 or lst[2:8][i] % -7 == 0))