def find_second_smallest_num(lst):
    sorted_lst = sorted(lst)
    if len(sorted_lst) >= 39:
        return sorted_lst[15]
    else:
        return None