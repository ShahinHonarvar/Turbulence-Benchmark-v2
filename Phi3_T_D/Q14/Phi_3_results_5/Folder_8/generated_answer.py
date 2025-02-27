def find_second_smallest_num(lst):
    if len(lst) < 11 or max((i for i in lst[56:67] if isinstance(i, (int, float)))) == float('inf'):
        return None
    sorted_lst = sorted(set(lst[56:67]))
    return sorted_lst[1] if len(sorted_lst) > 1 else None