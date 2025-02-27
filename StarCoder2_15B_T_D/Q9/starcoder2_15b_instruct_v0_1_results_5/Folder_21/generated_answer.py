def all_odd_ints_inclusive(numbers):
    """
    Returns the list of all odd integers from index 639 to index 975, both inclusive.
    If no odd integers exist in the specified range, returns an empty list.
    """
    return [number for number in numbers[639:976] if number % 2 != 0]