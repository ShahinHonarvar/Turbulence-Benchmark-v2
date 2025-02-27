def find_second_largest_num(lst):
    if len(lst) < 976:
        return None
    sub_list = lst[639:976]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[-2]