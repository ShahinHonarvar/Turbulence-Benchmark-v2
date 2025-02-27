def find_second_smallest_num(lst):
    if len(lst) < 67:
        return None
    sub_lst = lst[56:67]
    if len(sub_lst) < 2:
        return None
    sorted_lst = sorted(sub_lst)
    return sorted_lst[1]