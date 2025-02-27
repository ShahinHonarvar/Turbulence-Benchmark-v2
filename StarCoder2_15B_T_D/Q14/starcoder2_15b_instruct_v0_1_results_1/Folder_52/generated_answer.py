def find_second_smallest_num(lst):
    sublist = sorted(lst[64:67])
    return sublist[1] if len(sublist) == 3 else None