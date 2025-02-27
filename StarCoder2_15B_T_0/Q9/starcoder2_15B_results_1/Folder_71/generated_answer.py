def all_odd_ints_inclusive(numbers):
    """
    Returns the list of all odd integers from index 26 to index 52, both inclusive.
    If no odd integers exist in the specified range, an empty list is returned.
    """
    return [number for number in numbers[26:53] if number % 2 == 1]