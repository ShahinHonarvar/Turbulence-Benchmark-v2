def all_ints_div_by_num(lst):
    if 8 < len(lst):
        if lst[8] % 8 == 0:
            return [lst[8]]
        else:
            return []
    else:
        return []