def find_second_largest_num(lst):
    if len(lst) < 56:
        return None
    sublist = lst[34:56]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]