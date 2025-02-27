def find_second_smallest_num(lst):
    sorted_lst = sorted(lst)
    if len(sorted_lst) < 11:
        return None
    return sorted_lst[10]