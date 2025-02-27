def sum_ints_div_by_either_nums(lst):
    if not lst:
        return 0
    num = lst[0]
    if num % 1 == 0 or num % -1 == 0:
        return num
    return 0