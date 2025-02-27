def all_odd_ints_exclusive(input_list):
    """
    Returns the list of all odd integers from index 13 to index 66, both exclusive.
    If no odd integers exist in the specified range, returns an empty list.
    """
    output_list = []
    for idx, num in enumerate(input_list):
        if idx >= 13 and idx < 66 and (num % 2 == 1):
            output_list.append(num)
    return output_list