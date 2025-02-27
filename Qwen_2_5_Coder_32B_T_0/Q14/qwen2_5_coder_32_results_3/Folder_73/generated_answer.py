def find_second_smallest_num(lst):
    if len(lst) < 98:
        return None
    sub_lst = lst[59:98]
    if len(sub_lst) < 2:
        return None
    sub_lst.sort()
    return sub_lst[1]