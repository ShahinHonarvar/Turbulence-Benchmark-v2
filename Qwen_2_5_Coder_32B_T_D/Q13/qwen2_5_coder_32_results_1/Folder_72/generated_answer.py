def find_second_largest_num(lst):
    if len(lst) < 52:
        return None
    sublist = lst[29:52]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]