def find_second_smallest_num(lst):
    if len(lst) < 9:
        return None
    sublist = lst[:9]
    sublist.sort()
    if len(sublist) < 2:
        return None
    return sublist[1]