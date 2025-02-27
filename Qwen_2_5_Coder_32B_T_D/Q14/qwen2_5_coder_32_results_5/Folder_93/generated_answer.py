def find_second_smallest_num(lst):
    if len(lst) < 89:
        return None
    sublist = lst[75:89]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]