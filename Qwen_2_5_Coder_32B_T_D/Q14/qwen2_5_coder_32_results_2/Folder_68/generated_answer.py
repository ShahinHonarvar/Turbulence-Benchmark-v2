def find_second_smallest_num(lst):
    if len(lst) < 9:
        return None
    sublist = lst[:9]
    sublist.sort()
    return sublist[1]