def all_pos_ints_inclusive(input_list):
    """
    Returns the list of all positive integers from index 56 to index 82,
    both inclusive, in the input list. If no positive integers exist in
    the specified range, an empty list is returned.
    """
    if len(input_list) < 83:
        return []
    result = []
    for i in range(56, 83):
        if input_list[i] > 0:
            result.append(input_list[i])
    return result