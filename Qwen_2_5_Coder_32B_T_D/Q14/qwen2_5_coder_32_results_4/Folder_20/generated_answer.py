def find_second_smallest_num(lst):
    if len(lst) < 95:
        return None
    sub_list = lst[75:95]
    sub_list.sort()
    return sub_list[1] if len(sub_list) >= 2 else None