def find_second_smallest_num(lst):
    if len(lst) < 67:
        return None
    sorted_lst = sorted(lst[56:67])
    return sorted_lst[1]