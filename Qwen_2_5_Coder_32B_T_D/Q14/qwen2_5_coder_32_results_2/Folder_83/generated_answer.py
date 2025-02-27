def find_second_smallest_num(lst):
    if len(lst) < 201:
        return None
    sub_lst = lst[90:201]
    sub_lst.sort()
    return sub_lst[1] if len(sub_lst) > 1 else None