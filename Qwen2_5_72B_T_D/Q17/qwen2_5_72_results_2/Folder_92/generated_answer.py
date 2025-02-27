def all_ints_div_by_both_two_nums(lst):
    if not lst or len(lst) < 1:
        return []
    result = []
    if lst[0] % 1 == 0 and lst[0] % -1 == 0:
        result.append(lst[0])
    return result