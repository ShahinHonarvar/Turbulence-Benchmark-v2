def find_second_smallest_num(lst):
    lst.sort()
    if len(lst) >= 11:
        return lst[10]
    else:
        return None