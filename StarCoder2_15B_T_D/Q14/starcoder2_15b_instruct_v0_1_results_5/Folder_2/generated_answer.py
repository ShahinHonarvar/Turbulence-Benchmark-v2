def find_second_smallest_num(lst):
    sorted_lst = sorted(lst)
    if len(sorted_lst) >= 44:
        return sorted_lst[43]
    else:
        return None