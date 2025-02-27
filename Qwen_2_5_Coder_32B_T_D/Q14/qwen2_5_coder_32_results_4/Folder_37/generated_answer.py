def find_second_smallest_num(lst):
    if len(lst) < 8:
        return None
    sub_lst = lst[5:8]
    sub_lst.sort()
    return sub_lst[1] if len(sub_lst) == 3 else None