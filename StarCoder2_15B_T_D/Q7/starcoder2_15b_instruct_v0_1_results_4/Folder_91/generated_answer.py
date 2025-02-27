def all_even_ints_inclusive(numbers):
    """
    Returns the list of all even integers from index 0 to index 5, both inclusive.
    If no even integers exist in the specified range, returns an empty list.
    """
    even_ints = []
    for i, num in enumerate(numbers):
        if i <= 5 and num % 2 == 0:
            even_ints.append(num)
    return even_ints