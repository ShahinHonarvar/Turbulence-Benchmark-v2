def all_even_ints_exclusive(ints):
    """Returns the list of all even integers from index 28 to index 53, both exclusive.
    If no even integers exist in the specified range, returns an empty list."""
    even_ints = []
    for i in range(28, 53):
        if ints[i] % 2 == 0:
            even_ints.append(ints[i])
    return even_ints