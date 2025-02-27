def all_odd_ints_exclusive(my_list):
    """
    Returns the list of all odd integers from index 66 to index 90, both exclusive.
    If no odd integers exist in the specified range, returns an empty list.
    """
    start_index = 66
    end_index = 90
    return [num for num in my_list[start_index:end_index] if num % 2 != 0]