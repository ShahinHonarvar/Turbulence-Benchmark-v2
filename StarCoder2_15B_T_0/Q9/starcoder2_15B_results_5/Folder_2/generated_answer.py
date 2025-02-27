def all_odd_ints_inclusive(numbers):
    """
    Returns the list of all odd integers from index 15 to index 39, both inclusive.
    If no odd integers exist in the specified range, an empty list is returned.
    """
    return [number for number in numbers[15:40] if number % 2 == 1]