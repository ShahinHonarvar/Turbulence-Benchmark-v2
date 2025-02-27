def find_second_smallest_num(lst):
    sublist = sorted(lst[68:87])
    return sublist[1] if len(sublist) > 1 else None