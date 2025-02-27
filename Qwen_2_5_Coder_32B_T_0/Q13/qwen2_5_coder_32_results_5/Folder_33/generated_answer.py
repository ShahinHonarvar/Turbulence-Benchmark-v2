def find_second_largest_num(lst):
    if len(lst) < 775:
        return None
    sub_lst = lst[667:775]
    if len(sub_lst) < 2:
        return None
    sub_lst.sort()
    return sub_lst[-2]