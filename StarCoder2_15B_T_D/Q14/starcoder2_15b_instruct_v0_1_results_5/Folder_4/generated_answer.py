def find_second_smallest_num(input_list):
    """
    Find the second smallest element from index 70 to 84, both inclusive.
    If there is no such an element, return None.
    """
    sorted_list = sorted(input_list)
    if len(sorted_list) < 85:
        return None
    return sorted_list[84]