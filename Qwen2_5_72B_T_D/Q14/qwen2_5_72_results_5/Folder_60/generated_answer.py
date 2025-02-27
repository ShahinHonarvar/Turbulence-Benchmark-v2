def find_second_smallest_num(lst):
    if len(lst) < 99 or len(lst) < 57:
        return None
    sub_list = lst[56:99]
    sub_list.sort()
    return sub_list[1] if len(sub_list) > 1 else None