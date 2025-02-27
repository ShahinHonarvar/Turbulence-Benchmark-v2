def all_odd_ints_inclusive(input_list):
    """Returns the list of all odd integers from index 14 to index 64, both inclusive."""
    return [x for i, x in enumerate(input_list) if i >= 14 and i <= 64 and (x % 2 == 1)]