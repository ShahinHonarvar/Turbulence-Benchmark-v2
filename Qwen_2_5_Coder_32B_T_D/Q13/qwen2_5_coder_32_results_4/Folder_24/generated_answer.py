def find_second_largest_num(lst):
    if len(lst) < 96:
        return None
    sublist = lst[74:96]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]