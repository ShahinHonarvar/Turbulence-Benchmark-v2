def find_second_largest_num(lst):
    if len(lst) < 67:
        return None
    sub_lst = lst[64:67]
    if len(sub_lst) < 2:
        return None
    sub_lst.sort()
    return sub_lst[1]