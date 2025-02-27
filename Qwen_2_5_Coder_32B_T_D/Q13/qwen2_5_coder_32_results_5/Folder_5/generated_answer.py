def find_second_largest_num(lst):
    if len(lst) < 10:
        return None
    sub_lst = lst[8:10]
    if len(sub_lst) < 2:
        return None
    sorted_sub_lst = sorted(sub_lst)
    return sorted_sub_lst[-2]