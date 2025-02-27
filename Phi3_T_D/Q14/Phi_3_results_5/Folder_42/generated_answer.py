def find_second_smallest_num(lst):
    if len(lst[21:98]) < 2:
        return None
    minimum = min(lst[21:98])
    second_minimums = [x for x in lst[21:98] if x > minimum]
    return min(second_minimums) if second_minimums else None