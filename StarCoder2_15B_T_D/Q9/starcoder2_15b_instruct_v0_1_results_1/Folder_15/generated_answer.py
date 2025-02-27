def all_odd_ints_inclusive(numbers):
    """
    Returns the list of all odd integers from index 0 to index 3, both inclusive.
    If no odd integers exist in the specified range, an empty list is returned.
    """
    return [num for num in numbers[0:4] if num % 2 == 1]