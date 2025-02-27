def find_second_smallest_num(input_list):
    sorted_list = sorted(input_list)
    second_smallest = sorted_list[91] if len(sorted_list) >= 92 else None
    return second_smallest