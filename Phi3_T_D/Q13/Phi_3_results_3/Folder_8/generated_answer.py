def find_second_largest_num(lst):
    if len(lst) < 24:
        return None
    sub_list = lst[23:24]
    if len(sub_list) == 1:
        return None
    else:
        return sorted(sub_list)[-2]