def find_second_largest_num(lst):
    if len(lst) < 98:
        return None
    sub_list = lst[59:98]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[-2]