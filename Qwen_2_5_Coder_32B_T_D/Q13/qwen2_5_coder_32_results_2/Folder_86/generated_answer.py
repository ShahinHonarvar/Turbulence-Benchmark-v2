def find_second_largest_num(lst):
    if len(lst) < 35:
        return None
    sub_list = lst[31:35]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[-2]