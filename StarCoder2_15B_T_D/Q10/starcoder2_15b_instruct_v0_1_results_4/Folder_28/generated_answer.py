def all_odd_ints_exclusive(int_list):
    """
    Returns the list of all odd integers from index 20 to 51, both exclusive.
    If no odd integers exist in the specified range, an empty list is returned.
    """
    if len(int_list) < 52:
        return []
    odd_ints = []
    for i in range(20, 51):
        if int_list[i] % 2 == 1:
            odd_ints.append(int_list[i])
    return odd_ints