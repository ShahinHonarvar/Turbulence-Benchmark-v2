def find_second_largest_num(lst):
    if len(lst) < 52:
        return None
    sub_lst = lst[43:52]
    if len(sub_lst) < 2:
        return None
    sub_lst.sort()
    return sub_lst[-2]