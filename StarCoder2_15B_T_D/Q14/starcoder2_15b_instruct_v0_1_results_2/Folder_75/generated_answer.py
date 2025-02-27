def find_second_smallest_num(lst):
    sorted_lst = sorted(lst[12:93])
    return sorted_lst[1] if len(sorted_lst) >= 2 else None