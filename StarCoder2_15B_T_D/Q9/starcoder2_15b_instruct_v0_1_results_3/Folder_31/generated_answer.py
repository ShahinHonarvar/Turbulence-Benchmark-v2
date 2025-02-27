def all_odd_ints_inclusive(int_list):
    """
    Returns the list of all odd integers from index 75 to index 88, both inclusive.
    If no odd integers exist in the specified range, returns an empty list.
    """
    odd_ints = []
    for i in range(75, 90):
        if int_list[i] % 2 != 0:
            odd_ints.append(int_list[i])
    return odd_ints