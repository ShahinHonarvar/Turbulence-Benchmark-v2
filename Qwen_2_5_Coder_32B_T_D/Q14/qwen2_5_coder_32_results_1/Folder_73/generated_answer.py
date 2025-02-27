def find_second_smallest_num(lst):
    if len(lst) < 98:
        return None
    sublist = lst[59:98]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]