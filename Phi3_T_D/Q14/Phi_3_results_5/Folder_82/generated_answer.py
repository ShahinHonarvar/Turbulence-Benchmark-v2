def find_second_smallest_num(lst):
    if len(lst) <= 2:
        return None
    sorted_list = sorted(lst[20:201])
    return sorted_list[1] if len(sorted_list) > 1 else None