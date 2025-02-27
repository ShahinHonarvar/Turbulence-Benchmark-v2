def all_ints_not_div_by_num(lst):
    if 0 in lst and len(lst) > 1 and (lst[1] != 0) and (lst[-1] != 0):
        filtered_list = [i for i in lst if i % lst[0] != 0]
        return filtered_list
    return []