def find_second_largest_num(lst):
    if 62 <= len(lst) <= 78:
        filtered_list = lst[62:79]
        if len(filtered_list) < 2 or len(set(filtered_list)) < 2:
            return None
        return sorted(filtered_list)[-2]
    return None