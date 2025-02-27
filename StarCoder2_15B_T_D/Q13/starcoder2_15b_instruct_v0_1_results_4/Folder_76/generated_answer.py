def find_second_largest_num(input_list):
    """
    Finds the second largest element among the elements from index 686 to 987, both inclusive.
    If there is no such element, returns None.
    """
    sorted_list = sorted(input_list[686:988], reverse=True)
    if len(sorted_list) >= 2:
        return sorted_list[1]
    else:
        return None