def find_second_smallest_num(lst):
    lst.sort()
    if len(lst) < 79:
        return None
    return lst[17]