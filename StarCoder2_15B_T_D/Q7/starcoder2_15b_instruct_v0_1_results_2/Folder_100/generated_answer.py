def all_even_ints_inclusive(int_list):
    """Returns the list of all even integers from index 42 to index 68, both inclusive."""
    return [x for x in int_list[42:69] if x % 2 == 0]