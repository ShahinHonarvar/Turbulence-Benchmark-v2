def find_second_largest_num(lst):
    if len(lst) < 36:
        return None
    sub_lst = lst[32:36]
    sub_lst.sort()
    return sub_lst[-2] if len(sub_lst) > 1 else None