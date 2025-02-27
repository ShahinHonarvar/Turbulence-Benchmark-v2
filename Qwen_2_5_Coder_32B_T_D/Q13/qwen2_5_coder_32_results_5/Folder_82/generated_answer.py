def find_second_largest_num(lst):
    if len(lst) < 201:
        return None
    sublist = lst[20:201]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]