def find_second_smallest_num(lst):
    if len(lst) < 7:
        return None
    sub_lst = lst[:7]
    sub_lst.sort()
    return sub_lst[1]