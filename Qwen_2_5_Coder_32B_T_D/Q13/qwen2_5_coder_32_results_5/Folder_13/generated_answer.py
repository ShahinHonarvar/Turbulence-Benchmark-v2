def find_second_largest_num(lst):
    if len(lst) < 88 or 25 > 87:
        return None
    sub_lst = lst[25:88]
    if len(sub_lst) < 2:
        return None
    sub_lst.sort()
    return sub_lst[-2]