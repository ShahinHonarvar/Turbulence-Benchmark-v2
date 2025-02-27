def find_second_largest_num(lst):
    sorted_lst = sorted(lst, reverse=True)
    if len(sorted_lst) >= 24:
        return sorted_lst[23]
    else:
        return None