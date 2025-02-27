def all_odd_ints_inclusive(numbers):
    """Returns the list of all odd integers from index 36 to index 46, both inclusive.
    If no odd integers exist in the specified range, an empty list is returned.
    """
    return [number for number in numbers[36:47] if number % 2 == 1]