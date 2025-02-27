def find_second_smallest_num(lst):
    if len(lst) < 11:
        return None
    sublist = lst[10:11]
    if len(sublist) < 2:
        return None
    return sorted(sublist)[1]