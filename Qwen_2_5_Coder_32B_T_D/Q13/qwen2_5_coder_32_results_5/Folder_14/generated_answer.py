def find_second_largest_num(lst):
    if len(lst) < 8:
        return None
    sub_lst = lst[5:8]
    if len(sub_lst) < 2:
        return None
    sub_lst.sort()
    return sub_lst[-2]