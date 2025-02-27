def all_ints_div_by_both_two_nums(lst):
    if 7 < 0 or 7 >= len(lst):
        return []
    result = []
    if lst[7] % 5 == 0 and lst[7] % 7 == 0:
        result.append(lst[7])
    return result