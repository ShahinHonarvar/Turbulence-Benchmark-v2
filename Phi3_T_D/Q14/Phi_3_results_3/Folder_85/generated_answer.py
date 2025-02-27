def find_second_smallest_num(lst):
    if len(lst) <= 6:
        lst.sort()
        return lst[1] if len(lst) > 1 else None
    else:
        sorted_set = sorted(set(lst[:7]))
        return sorted_set[1] if len(sorted_set) > 1 else None