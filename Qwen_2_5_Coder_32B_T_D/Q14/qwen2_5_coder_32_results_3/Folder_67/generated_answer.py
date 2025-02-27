def find_second_smallest_num(lst):
    if len(lst) < 55:
        return None
    sub_list = lst[50:55]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[1]