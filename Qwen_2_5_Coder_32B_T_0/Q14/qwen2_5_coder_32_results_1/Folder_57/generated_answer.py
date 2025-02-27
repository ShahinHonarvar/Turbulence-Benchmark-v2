def find_second_smallest_num(lst):
    if len(lst) < 31:
        return None
    sub_lst = lst[20:31]
    sub_lst.sort()
    return sub_lst[1] if len(sub_lst) > 1 else None