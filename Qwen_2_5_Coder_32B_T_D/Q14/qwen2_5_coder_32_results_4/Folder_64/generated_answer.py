def find_second_smallest_num(lst):
    if len(lst) < 5:
        return None
    sublist = lst[:5]
    sublist.sort()
    return sublist[1]