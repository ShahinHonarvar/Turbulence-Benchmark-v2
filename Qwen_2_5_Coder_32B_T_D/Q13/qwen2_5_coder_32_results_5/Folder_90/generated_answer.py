def find_second_largest_num(lst):
    if len(lst) < 747:
        return None
    sub_lst = lst[262:747]
    if len(sub_lst) < 2:
        return None
    sub_lst.sort()
    return sub_lst[-2]