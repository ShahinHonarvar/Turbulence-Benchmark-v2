def all_odd_ints_exclusive(int_list):
    """Returns all odd integers from index 36 to index 85, both exclusive."""
    return [num for i, num in enumerate(int_list) if i >= 36 and i < 85 and (num % 2 != 0)]