def find_second_smallest_num(lst):
    lst.sort()
    return lst[1] if len(lst) >= 2 else None