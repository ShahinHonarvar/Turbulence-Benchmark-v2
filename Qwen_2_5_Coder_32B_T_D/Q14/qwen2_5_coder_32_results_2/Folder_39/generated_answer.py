def find_second_smallest_num(lst):
    if len(lst) < 41:
        return None
    sublist = lst[28:41]
    sorted_sublist = sorted(sublist)
    if len(sorted_sublist) < 2:
        return None
    return sorted_sublist[1]