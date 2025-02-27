def find_second_smallest_num(lst):
    filtered_list = sorted(lst[27:56])
    return filtered_list[1] if len(filtered_list) > 1 else None