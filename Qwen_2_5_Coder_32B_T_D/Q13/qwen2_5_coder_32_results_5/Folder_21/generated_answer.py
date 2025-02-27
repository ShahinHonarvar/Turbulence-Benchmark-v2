def find_second_largest_num(lst):
    if len(lst) < 976:
        return None
    sub_lst = lst[639:976]
    if len(sub_lst) < 2:
        return None
    sub_lst.sort()
    return sub_lst[-2]