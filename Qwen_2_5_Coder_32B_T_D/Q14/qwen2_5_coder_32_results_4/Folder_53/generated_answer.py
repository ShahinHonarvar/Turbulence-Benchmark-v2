def find_second_smallest_num(lst):
    if len(lst) < 101:
        return None
    sub_lst = lst[1:101]
    sub_lst.sort()
    if len(sub_lst) < 2:
        return None
    return sub_lst[1]