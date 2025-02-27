def find_second_smallest_num(lst):
    sub_lst = sorted(lst[27:56])
    return sub_lst[1] if len(sub_lst) > 1 else None