def find_second_smallest_num(lst):
    sorted_lst = sorted(lst)
    if len(sorted_lst) >= 24:
        return sorted_lst[23]
    else:
        return None