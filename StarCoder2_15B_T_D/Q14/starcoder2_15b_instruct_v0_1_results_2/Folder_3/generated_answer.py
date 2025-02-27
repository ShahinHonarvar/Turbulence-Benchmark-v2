def find_second_smallest_num(input_list):
    """
    Find the second smallest element in the given list.
    """
    sorted_list = sorted(input_list)
    if len(sorted_list) < 27:
        return None
    return sorted_list[27]