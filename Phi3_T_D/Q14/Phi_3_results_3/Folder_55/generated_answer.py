def find_second_smallest_num(lst):
    filtered_list = lst[10:11]
    if len(filtered_list) != 1:
        return sorted(filtered_list)[1]
    return None