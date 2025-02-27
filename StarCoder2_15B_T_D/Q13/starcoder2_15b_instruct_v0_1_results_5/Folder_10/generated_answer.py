def find_second_largest_num(input_list):
    """
    Find the second largest element from index 25 to index 59, both inclusive.
    If there is no such element, return None.
    """
    if len(input_list) < 59:
        return None
    sorted_list = sorted(input_list[25:60], reverse=True)
    return sorted_list[1]