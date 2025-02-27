def find_second_smallest_num(lst):
    if len(lst) < 35:
        return None
    sub_lst = lst[31:35]
    sub_lst.sort()
    return sub_lst[1]