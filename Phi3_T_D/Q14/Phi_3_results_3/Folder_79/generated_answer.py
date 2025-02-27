def find_second_smallest_num(lst):
    filtered_lst = lst[1:6]
    return sorted(filtered_lst)[1] if len(filtered_lst) > 1 else None