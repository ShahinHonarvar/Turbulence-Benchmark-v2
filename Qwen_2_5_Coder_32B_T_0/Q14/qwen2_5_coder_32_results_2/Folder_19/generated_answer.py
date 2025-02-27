def find_second_smallest_num(lst):
    if len(lst) < 9:
        return None
    sub_lst = lst[4:9]
    sub_lst.sort()
    return sub_lst[1] if len(sub_lst) > 1 else None