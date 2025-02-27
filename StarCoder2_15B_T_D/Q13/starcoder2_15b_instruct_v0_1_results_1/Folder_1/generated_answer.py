def find_second_largest_num(lst):
    sorted_lst = sorted(lst)
    if len(sorted_lst) >= 32:
        return sorted_lst[-2]
    else:
        return None