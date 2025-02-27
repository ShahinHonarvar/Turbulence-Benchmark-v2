def find_second_largest_num(lst):
    sub_list = lst[29:52]
    if len(sub_list) < 2:
        return None
    sub_list.sort(reverse=True)
    return sub_list[1] if len(sub_list) > 1 else None