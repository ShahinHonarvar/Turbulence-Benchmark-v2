def sum_ints_div_by_either_nums(lst):
    result = sum((lst[i] for i in range(18, 53) if lst[i] % 15 == 0 or lst[i] % 57 == 0))
    return result