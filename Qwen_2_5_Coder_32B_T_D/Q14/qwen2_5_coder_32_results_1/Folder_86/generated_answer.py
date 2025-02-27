def find_second_smallest_num(lst):
    if len(lst) >= 37:
        sub_lst = lst[33:37]
        sub_lst.sort()
        return sub_lst[1]
    return None