def find_second_smallest_num(lst):
    if len(lst) < 88:
        return None
    sub_list = lst[30:88]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[1]