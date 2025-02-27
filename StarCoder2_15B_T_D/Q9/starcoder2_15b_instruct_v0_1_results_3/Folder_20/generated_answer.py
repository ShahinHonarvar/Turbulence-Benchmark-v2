def all_odd_ints_inclusive(numbers):
    """
    Returns the list of all odd integers from index 56 to index 66, both inclusive.
    If no odd integers exist in the specified range, returns an empty list.
    """
    return [num for num in numbers[56:67] if num % 2 == 1]