def find_second_smallest_num(lst):
    sorted_lst = sorted(lst)
    if len(sorted_lst) >= 66:
        return sorted_lst[66]
    else:
        return None