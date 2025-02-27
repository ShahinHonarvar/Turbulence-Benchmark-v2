def find_second_smallest_num(lst):
    if len(lst) < 751:
        return None
    sub_lst = lst[246:751]
    sorted_sub_lst = sorted(sub_lst)
    return sorted_sub_lst[1] if len(sorted_sub_lst) > 1 else None