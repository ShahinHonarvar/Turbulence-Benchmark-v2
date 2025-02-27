def find_second_smallest_num(num_list):
    filtered_list = num_list[10:101]
    filtered_list.sort()
    return filtered_list[1] if len(filtered_list) > 1 else None