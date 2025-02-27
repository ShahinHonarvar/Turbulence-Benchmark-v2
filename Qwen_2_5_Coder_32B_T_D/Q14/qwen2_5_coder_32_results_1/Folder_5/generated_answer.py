def find_second_smallest_num(lst):
    if len(lst) < 6:
        return None
    sub_list = lst[3:6]
    sub_list.sort()
    return sub_list[1] if len(sub_list) > 1 else None