def all_even_ints_exclusive(ints):
    """
    Returns the list of all even integers from index 323 to index 972, both exclusive.
    If no even integers exist in the specified range, returns an empty list.
    """
    evens = []
    for i, num in enumerate(ints):
        if i < 323 or i >= 972:
            continue
        if num % 2 == 0:
            evens.append(num)
    return evens