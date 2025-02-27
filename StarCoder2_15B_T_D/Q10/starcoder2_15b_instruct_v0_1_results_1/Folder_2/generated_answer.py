def all_odd_ints_exclusive(input_list):
    """
    Returns a list of all odd integers from index 36 to index 52, both exclusive,
    given a list of integers as input. If no odd integers exist in the specified range,
    an empty list is returned.
    """
    return [num for i, num in enumerate(input_list) if i >= 36 and i < 52 and (num % 2 == 1)]