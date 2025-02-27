def all_even_ints_inclusive(lst):
    """
    Returns the list of all even integers from index 40 to index 80, both inclusive.
    If no even integers exist in the specified range, an empty list is returned.
    """
    even_ints = []
    for i, num in enumerate(lst):
        if i >= 40 and i <= 80 and (num % 2 == 0):
            even_ints.append(num)
    return even_ints