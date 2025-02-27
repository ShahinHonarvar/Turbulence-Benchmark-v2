def find_second_smallest_num(lst):
    sorted_lst = sorted(lst)
    if len(sorted_lst) >= 8:
        return sorted_lst[1]
    else:
        return None