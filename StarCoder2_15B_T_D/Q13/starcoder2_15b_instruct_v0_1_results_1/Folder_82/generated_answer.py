def find_second_largest_num(lst):
    sorted_lst = sorted(lst, reverse=True)
    if len(sorted_lst) >= 21:
        return sorted_lst[20]
    else:
        return None