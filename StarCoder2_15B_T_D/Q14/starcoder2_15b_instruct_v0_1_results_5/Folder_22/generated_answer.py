def find_second_smallest_num(lst):
    sorted_lst = sorted(lst)
    if len(sorted_lst) >= 41:
        return sorted_lst[40]
    else:
        return None