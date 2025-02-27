def find_second_largest_num(lst):
    if len(lst) < 89:
        return None
    sub_lst = lst[75:89]
    if len(sub_lst) < 2:
        return None
    sub_lst.sort()
    return sub_lst[-2]