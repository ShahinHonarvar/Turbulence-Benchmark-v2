def find_second_smallest_num(input_list):
    """Find the second smallest element from index 31 to 34, both inclusive."""
    if len(input_list) < 34:
        return None
    sorted_list = sorted(input_list[31:35])
    return sorted_list[1]