def find_second_smallest_num(lst):
    sorted_lst = sorted(lst)
    if len(sorted_lst) >= 371:
        return sorted_lst[310]
    else:
        return None