def find_second_largest_num(lst):
    if len(lst) < 83:
        return None
    sub_list = lst[56:83]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[-2]