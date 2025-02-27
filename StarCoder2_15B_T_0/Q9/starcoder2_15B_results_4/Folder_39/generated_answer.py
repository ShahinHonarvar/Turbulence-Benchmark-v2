def all_odd_ints_inclusive(numbers):
    """
    Returns the list of all odd integers from index 20 to index 30, both inclusive.
    If no odd integers exist in the specified range, an empty list is returned.
    """
    return [number for number in numbers[20:31] if number % 2 == 1]