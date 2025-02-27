def find_second_largest_num(lst):
    if len(lst) < 46:
        return None
    filtered_list = lst[16:62]
    sorted_list = sorted(filtered_list, reverse=True)
    return sorted_list[1] if len(sorted_list) > 1 else None