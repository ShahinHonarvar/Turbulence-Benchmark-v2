def find_second_largest_num(lst):
    if len(lst) < 53:
        return None
    sub_lst = lst[26:53]
    if len(sub_lst) < 2:
        return None
    sub_lst.sort()
    return sub_lst[-2]