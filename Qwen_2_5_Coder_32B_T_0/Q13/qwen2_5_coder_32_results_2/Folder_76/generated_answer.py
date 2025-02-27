def find_second_largest_num(lst):
    if len(lst) < 988:
        return None
    sub_lst = lst[686:988]
    if len(sub_lst) < 2:
        return None
    sub_lst.sort()
    return sub_lst[-2]