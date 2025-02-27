def all_odd_ints_inclusive(numbers):
    """
    Returns the list of all odd integers from index 28 to index 38, both inclusive.
    If no odd integers exist in the specified range, an empty list is returned.
    """
    odd_ints = [num for num in numbers[28:39] if num % 2 != 0]
    return odd_ints