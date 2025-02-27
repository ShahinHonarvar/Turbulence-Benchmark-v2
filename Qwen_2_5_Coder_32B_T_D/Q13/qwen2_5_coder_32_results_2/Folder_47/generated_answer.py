def find_second_largest_num(lst):
    if len(lst) <= 76 or max(37, 76) >= len(lst):
        return None
    sub_lst = lst[37:77]
    if len(sub_lst) < 2:
        return None
    sub_lst.sort()
    return sub_lst[-2]