def find_second_smallest_num(lst):
    if len(lst) < 201:
        return None
    sublist = lst[30:201]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]