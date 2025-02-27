def find_second_largest_num(lst):
    sorted_lst = sorted(lst, reverse=True)
    if len(sorted_lst) >= 36:
        return sorted_lst[36]
    else:
        return None