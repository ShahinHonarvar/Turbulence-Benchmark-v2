def find_second_smallest_num(lst):
    if len(lst) < 5:
        return None
    sublist = lst[4:5]
    if len(sublist) < 2:
        return None
    sorted_sublist = sorted(sublist)
    return sorted_sublist[1]