def all_odd_ints_inclusive(int_list):
    """Returns the list of all odd integers from index 27 to index 55, both inclusive. If no odd integers exist in the specified range, returns an empty list."""
    return [i for i in int_list[27:56] if i % 2 == 1]