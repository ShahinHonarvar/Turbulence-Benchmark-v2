def find_second_largest_num(lst):
    if len(lst) < 6:
        return None
    sub_lst = lst[1:6]
    sub_lst.sort()
    return sub_lst[-2]