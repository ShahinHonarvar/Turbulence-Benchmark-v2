def find_second_smallest_num(lst):
    if len(lst) < 7:
        return None
    sub_lst = lst[6:7]
    if len(sub_lst) < 2:
        return None
    return sorted(sub_lst)[1]