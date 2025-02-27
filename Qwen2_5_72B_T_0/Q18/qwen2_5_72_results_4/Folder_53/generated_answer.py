def sum_ints_div_by_either_nums(lst):
    if len(lst) < 201:
        return 0
    num = lst[200]
    if num % 17 == 0 or num % -5 == 0:
        return num
    return 0