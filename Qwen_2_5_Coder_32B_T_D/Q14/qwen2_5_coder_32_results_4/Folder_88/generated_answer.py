def find_second_smallest_num(lst):
    if len(lst) < 9:
        return None
    sublist = lst[6:9]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]