def all_odd_ints_inclusive(numbers):
    """Returns the list of all odd integers from index 56 to index 57, both inclusive.
    If no odd integers exist in the specified range, an empty list is returned.
    """
    return [number for number in numbers[56:58] if number % 2 == 1]