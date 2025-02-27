def all_odd_ints_exclusive(my_list):
    """Returns the list of all odd integers from index 18 to index 60, both exclusive. If no odd integers exist in the specified range, returns an empty list."""
    return [i for i in my_list[18:60] if i % 2 == 1]