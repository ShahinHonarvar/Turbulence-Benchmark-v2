def find_second_largest_num(lst):
    sorted_lst = sorted(lst, reverse=True)
    if len(sorted_lst) >= 6:
        return sorted_lst[4]
    else:
        return None