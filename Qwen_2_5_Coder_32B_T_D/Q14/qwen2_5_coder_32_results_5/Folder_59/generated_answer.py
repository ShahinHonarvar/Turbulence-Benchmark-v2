def find_second_smallest_num(lst):
    if len(lst) < 10:
        return None
    sub_lst = lst[:10]
    sub_lst.sort()
    return sub_lst[1]