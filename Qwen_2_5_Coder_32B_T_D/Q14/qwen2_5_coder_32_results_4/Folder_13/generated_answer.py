def find_second_smallest_num(lst):
    if len(lst) < 33:
        return None
    sublist = lst[28:33]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]