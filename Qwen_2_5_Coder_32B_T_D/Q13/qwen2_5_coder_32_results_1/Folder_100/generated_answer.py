def find_second_largest_num(lst):
    if len(lst) <= 68 or 42 >= len(lst):
        return None
    sub_lst = lst[42:69]
    if len(sub_lst) < 2:
        return None
    sub_lst.sort()
    return sub_lst[-2]