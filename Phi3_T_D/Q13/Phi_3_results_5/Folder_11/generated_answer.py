def find_second_largest_num(lst):
    if len(lst) < 15:
        return None
    sub_list = sorted(lst[37:52], reverse=True)
    return sub_list[1] if len(sub_list) > 1 else None