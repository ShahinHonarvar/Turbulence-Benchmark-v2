def find_second_smallest_num(lst):
    if len(lst) <= 55:
        return None
    lst.sort()
    return lst[28]