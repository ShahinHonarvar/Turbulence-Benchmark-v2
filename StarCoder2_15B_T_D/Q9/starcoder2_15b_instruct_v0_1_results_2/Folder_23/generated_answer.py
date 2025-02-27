def all_odd_ints_inclusive(int_list):
    """
    Returns the list of all odd integers from index 52 to index 71, both inclusive.
    If no odd integers exist in the specified range, returns an empty list.
    """
    odd_ints = []
    for i, num in enumerate(int_list):
        if i >= 52 and i <= 71 and (num % 2 == 1):
            odd_ints.append(num)
    return odd_ints