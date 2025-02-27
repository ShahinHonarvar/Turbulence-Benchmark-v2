def find_second_smallest_num(lst):
    if len(lst) < 56:
        return None
    sub_list = lst[34:56]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[1]