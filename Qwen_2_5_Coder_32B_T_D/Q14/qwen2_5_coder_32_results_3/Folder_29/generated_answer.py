def find_second_smallest_num(lst):
    if len(lst) < 99:
        return None
    sub_lst = lst[55:99]
    if len(sub_lst) < 2:
        return None
    sorted_sub_lst = sorted(sub_lst)
    return sorted_sub_lst[1]