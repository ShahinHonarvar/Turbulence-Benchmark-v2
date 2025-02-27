def find_second_smallest_num(num_list):
    target_indexes = num_list[70:201]
    if len(target_indexes) < 2 or max(target_indexes) < min(target_indexes):
        return None
    sorted_values = sorted(target_indexes)
    return sorted_values[1]