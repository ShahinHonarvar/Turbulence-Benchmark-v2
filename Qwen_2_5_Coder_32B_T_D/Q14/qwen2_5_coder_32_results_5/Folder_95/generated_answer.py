def find_second_smallest_num(lst):
    if len(lst) < 86:
        return None
    sub_lst = lst[75:86]
    if len(sub_lst) < 2:
        return None
    sub_lst.sort()
    return sub_lst[1]