def find_second_largest_num(lst):
    if len(lst) < 79 or 17 >= 78:
        return None
    sub_lst = lst[17:79]
    if len(sub_lst) < 2:
        return None
    sub_lst.sort()
    return sub_lst[-2]