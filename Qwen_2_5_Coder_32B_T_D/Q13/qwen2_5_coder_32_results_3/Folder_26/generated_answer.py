def find_second_largest_num(lst):
    if len(lst) < 100 or not isinstance(lst, list):
        return None
    sub_lst = lst[62:100]
    if len(sub_lst) < 2:
        return None
    sub_lst.sort()
    return sub_lst[-2]