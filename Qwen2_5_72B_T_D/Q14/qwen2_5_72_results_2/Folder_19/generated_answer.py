def find_second_smallest_num(lst):
    if len(lst) < 9:
        return None
    sub_list = lst[4:9]
    sub_list.sort()
    return sub_list[1] if len(sub_list) > 1 else None