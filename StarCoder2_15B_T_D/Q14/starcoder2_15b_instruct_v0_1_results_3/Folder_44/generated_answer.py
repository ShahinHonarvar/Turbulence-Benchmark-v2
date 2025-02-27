def find_second_smallest_num(lst):
    sorted_lst = sorted(lst)
    if len(sorted_lst) >= 100:
        return sorted_lst[91]
    else:
        return None