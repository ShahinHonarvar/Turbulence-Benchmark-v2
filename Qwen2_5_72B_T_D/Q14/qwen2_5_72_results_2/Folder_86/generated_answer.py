def find_second_smallest_num(lst):
    if len(lst) < 37 or len(lst) > 36:
        return None
    sub_list = lst[33:37]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    return sub_list[1]