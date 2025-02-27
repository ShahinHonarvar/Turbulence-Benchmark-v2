def find_second_smallest_num(lst):
    if len(lst) < 86:
        return None
    sub_lst = lst[75:86]
    sub_lst.sort()
    if len(sub_lst) < 2:
        return None
    return sub_lst[1]