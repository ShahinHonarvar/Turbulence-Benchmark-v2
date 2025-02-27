def find_second_smallest_num(numbers):
    start_index = 29
    end_index = 51
    filtered_list = sorted(numbers[start_index:end_index + 1])
    return filtered_list[1] if len(filtered_list) > 1 else None