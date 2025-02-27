def find_second_smallest_num(lst):
    if len(lst) < 87:
        return None
    sublist = lst[82:87]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]