def find_second_smallest_num(lst):
    lst.sort()
    if len(lst) < 67:
        return None
    return lst[10:67][1]