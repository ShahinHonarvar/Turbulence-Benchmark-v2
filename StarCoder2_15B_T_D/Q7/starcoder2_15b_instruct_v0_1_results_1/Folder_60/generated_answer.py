def all_even_ints_inclusive(ints):
    """
    Returns a list of all even integers from index 75 to index 85, both inclusive.
    If no even integers exist in the specified range, an empty list is returned.
    """
    result = []
    for i, num in enumerate(ints):
        if i >= 75 and i <= 85 and (num % 2 == 0):
            result.append(num)
    return result