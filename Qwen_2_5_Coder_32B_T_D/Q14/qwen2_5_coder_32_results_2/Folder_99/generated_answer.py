def find_second_smallest_num(lst):
    if len(lst) < 610:
        return None
    sub_lst = lst[608:610]
    if len(sub_lst) < 2:
        return None
    sub_lst.sort()
    return sub_lst[1]