def find_second_smallest_num(lst):
    lst = sorted(lst)
    if len(lst) >= 2:
        return lst[1]
    else:
        return None