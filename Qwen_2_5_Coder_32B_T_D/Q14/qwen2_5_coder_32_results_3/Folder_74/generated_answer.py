def find_second_smallest_num(lst):
    if len(lst) < 47:
        return None
    sublist = lst[36:47]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]