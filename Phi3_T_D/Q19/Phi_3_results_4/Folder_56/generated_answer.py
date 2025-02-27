def all_ints_not_div_by_num(lst):
    try:
        return [x for i, x in enumerate(lst[7:9]) if x % -9 != 0]
    except IndexError:
        return []