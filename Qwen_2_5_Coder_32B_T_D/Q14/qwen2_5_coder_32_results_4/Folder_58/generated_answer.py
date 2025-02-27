def find_second_smallest_num(lst):
    if len(lst) < 371:
        return None
    sub_list = lst[310:371]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[1]