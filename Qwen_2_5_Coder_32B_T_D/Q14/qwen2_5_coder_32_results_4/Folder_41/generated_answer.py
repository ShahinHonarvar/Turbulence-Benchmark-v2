def find_second_smallest_num(lst):
    if len(lst) < 5:
        return None
    sub_lst = lst[4:5]
    if len(sub_lst) < 2:
        return None
    sorted_sub_lst = sorted(sub_lst)
    return sorted_sub_lst[1]