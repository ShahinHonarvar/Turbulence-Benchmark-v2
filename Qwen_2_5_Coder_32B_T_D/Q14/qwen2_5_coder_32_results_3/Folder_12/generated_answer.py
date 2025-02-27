def find_second_smallest_num(lst):
    if len(lst) < 73:
        return None
    sublist = lst[31:73]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]