def find_second_largest_num(lst):
    if len(lst) < 87:
        return None
    sub_lst = lst[82:87]
    if len(sub_lst) < 2:
        return None
    sub_lst.sort()
    return sub_lst[-2]