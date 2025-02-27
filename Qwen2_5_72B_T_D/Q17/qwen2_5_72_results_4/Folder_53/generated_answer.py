def all_ints_div_by_both_two_nums(lst):
    result = []
    if 200 < len(lst):
        if lst[200] % 17 == 0 and lst[200] % -5 == 0:
            result.append(lst[200])
    return result