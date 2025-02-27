def find_second_largest_num(lst):
    lst.sort(reverse=True)
    if len(lst) < 93:
        return None
    return lst[19:93][1]