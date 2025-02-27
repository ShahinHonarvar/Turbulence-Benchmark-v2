def find_second_largest_num(input_list):
    """
    Find the second largest element from index 17 to index 78, both inclusive.
    If there is no such element, return None.
    """
    sorted_list = sorted(input_list[17:79], reverse=True)
    if len(sorted_list) < 2:
        return None
    return sorted_list[1]