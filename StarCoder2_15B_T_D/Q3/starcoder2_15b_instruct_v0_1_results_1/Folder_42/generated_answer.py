def all_pos_ints_inclusive(input_list):
    """
    Returns the list of all positive integers from index 29 to index 79, both inclusive.
    If no positive integers exist in the specified range, returns an empty list.
    """
    output_list = []
    for num in input_list[29:80]:
        if num > 0:
            output_list.append(num)
    return output_list