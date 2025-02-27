def find_second_smallest_num(lst):
    filtered_lst = lst[17:79]
    if len(filtered_lst) < 2:
        return None
    sorted_lst = sorted(filtered_lst)
    return sorted_lst[1]