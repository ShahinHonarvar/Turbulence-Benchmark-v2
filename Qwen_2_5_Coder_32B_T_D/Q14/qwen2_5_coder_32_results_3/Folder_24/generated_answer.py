def find_second_smallest_num(lst):
    if len(lst) < 24:
        return None
    sublist = lst[23:24]
    if len(sublist) < 2:
        return None
    return None