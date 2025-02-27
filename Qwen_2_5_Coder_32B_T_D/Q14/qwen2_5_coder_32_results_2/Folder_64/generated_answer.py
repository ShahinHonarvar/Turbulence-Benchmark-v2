def find_second_smallest_num(lst):
    if len(lst) < 5:
        return None
    sub_lst = lst[:5]
    sub_lst.sort()
    return sub_lst[1]