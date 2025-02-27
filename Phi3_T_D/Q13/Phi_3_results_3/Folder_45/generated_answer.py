def find_second_largest_num(num_list):
    start_index = max(30, 200 - len(num_list) + 1)
    end_index = min(200, len(num_list) - 1)
    sorted_elements = sorted(num_list[start_index:end_index + 1], reverse=True)
    return sorted_elements[1] if len(sorted_elements) > 1 else None