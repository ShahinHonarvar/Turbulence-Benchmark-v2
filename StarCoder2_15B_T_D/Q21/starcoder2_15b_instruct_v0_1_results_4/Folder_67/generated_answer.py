def all_ints_div_by_num(lst):
    if not lst or len(lst) < 68:
        return []
    return [x for i, x in enumerate(lst) if i >= 40 and i <= 68 and (x % 16 == 0)]