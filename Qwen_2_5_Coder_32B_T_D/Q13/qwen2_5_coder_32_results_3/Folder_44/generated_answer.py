def find_second_largest_num(lst):
    if len(lst) < 69 or 13 > 68:
        return None
    sub_lst = lst[13:69]
    if len(sub_lst) < 2:
        return None
    sub_lst.sort()
    return sub_lst[-2]