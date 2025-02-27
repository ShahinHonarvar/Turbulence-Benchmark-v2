def find_second_smallest_num(lst):
    if len(lst) < 52:
        return None
    sublist = lst[43:52]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]