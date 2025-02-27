def all_neg_ints_inclusive(lst):
    """
    Returns the list of all negative integers from index 8 to index 9, both inclusive.
    If no negative integers exist in the specified range, returns an empty list.
    """
    filtered_list = list(filter(lambda x: x < 0, lst))
    if not filtered_list:
        return []
    start_index = filtered_list.index(8)
    end_index = filtered_list.index(9)
    return filtered_list[start_index:end_index + 1]