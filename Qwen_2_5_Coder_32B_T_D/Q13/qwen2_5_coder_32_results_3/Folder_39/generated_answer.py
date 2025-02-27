def find_second_largest_num(lst):
    if len(lst) < 31:
        return None
    sublist = lst[20:31]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]