def find_second_largest_num(lst):
    if len(lst) < 86:
        return None
    sublist = lst[75:86]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]