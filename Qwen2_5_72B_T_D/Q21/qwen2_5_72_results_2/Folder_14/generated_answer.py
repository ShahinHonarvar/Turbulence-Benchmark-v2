def all_ints_div_by_num(lst):
    if len(lst) < 9:
        return []
    result = []
    if lst[8] % 8 == 0:
        result.append(lst[8])
    return result