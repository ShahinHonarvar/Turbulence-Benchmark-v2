def find_second_smallest_num(lst):
    if len(lst) < 201:
        return None
    sub_lst = lst[90:201]
    if len(sub_lst) < 2:
        return None
    sub_lst.sort()
    return sub_lst[1]