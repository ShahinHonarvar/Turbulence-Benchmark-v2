def find_second_smallest_num(lst):
    sorted_lst = sorted(lst)
    if len(sorted_lst) >= 58:
        return sorted_lst[57]
    else:
        return None