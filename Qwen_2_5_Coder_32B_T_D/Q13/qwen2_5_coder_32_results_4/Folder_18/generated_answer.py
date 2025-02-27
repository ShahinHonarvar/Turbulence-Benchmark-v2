def find_second_largest_num(lst):
    if len(lst) < 50:
        return None
    sublist = lst[35:50]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]