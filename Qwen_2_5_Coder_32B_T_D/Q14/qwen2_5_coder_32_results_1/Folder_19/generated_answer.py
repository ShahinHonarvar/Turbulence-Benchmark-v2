def find_second_smallest_num(lst):
    if len(lst) < 9:
        return None
    sub_lst = lst[4:9]
    sub_lst.sort()
    if len(sub_lst) < 2:
        return None
    return sub_lst[1]