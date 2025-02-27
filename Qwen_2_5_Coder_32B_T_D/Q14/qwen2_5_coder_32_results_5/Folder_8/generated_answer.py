def find_second_smallest_num(lst):
    if len(lst) < 67:
        return None
    sub_lst = lst[56:67]
    sub_lst.sort()
    return sub_lst[1] if len(sub_lst) > 1 else None