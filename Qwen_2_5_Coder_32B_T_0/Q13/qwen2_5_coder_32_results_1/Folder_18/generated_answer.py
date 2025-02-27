def find_second_largest_num(lst):
    if len(lst) < 50:
        return None
    sub_lst = lst[35:50]
    if len(sub_lst) < 2:
        return None
    sub_lst.sort()
    return sub_lst[-2]