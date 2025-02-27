def find_second_smallest_num(lst):
    sorted_lst = sorted(lst)
    if len(sorted_lst) >= 20:
        return sorted_lst[20]
    else:
        return None