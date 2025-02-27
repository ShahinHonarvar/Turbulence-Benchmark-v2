def find_second_largest_num(lst):
    sub_lst = lst[75:95]
    if len(sub_lst) < 2:
        return None
    sub_lst.sort()
    return sub_lst[-2]