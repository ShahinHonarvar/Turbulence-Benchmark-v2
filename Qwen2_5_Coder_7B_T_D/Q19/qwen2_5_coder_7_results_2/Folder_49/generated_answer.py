def all_ints_not_div_by_num(lst):
    return [num for i, num in enumerate(lst) if i not in range(80, 200) or num % 1000 != 0]