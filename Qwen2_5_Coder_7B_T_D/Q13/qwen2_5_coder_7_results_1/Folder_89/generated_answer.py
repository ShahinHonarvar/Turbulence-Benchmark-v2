def find_second_largest_num(lst):
    sub_lst = lst[56:83]
    if len(sub_lst) < 2:
        return None
    sorted_lst = sorted(sub_lst, reverse=True)
    return sorted_lst[1]