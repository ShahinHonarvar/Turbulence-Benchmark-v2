def find_second_smallest_num(lst):
    if len(lst) < 55:
        return None
    sub_lst = lst[50:55]
    if len(sub_lst) < 2:
        return None
    sub_lst.sort()
    return sub_lst[1]