def find_second_smallest_num(lst):
    if len(lst) <= 8:
        sorted_lst = sorted(lst[0:9])
        return sorted_lst[1] if len(sorted_lst) > 1 else None
    else:
        return None