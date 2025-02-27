def find_second_smallest_num(lst):
    if len(lst) < 88:
        return None
    sub_lst = lst[25:88]
    sub_lst.sort()
    if len(sub_lst) < 2:
        return None
    return sub_lst[1]