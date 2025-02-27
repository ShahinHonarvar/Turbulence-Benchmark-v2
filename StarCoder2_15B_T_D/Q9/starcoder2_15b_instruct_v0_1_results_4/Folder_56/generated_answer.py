def all_odd_ints_inclusive(numbers):
    """
    Returns the list of all odd integers from index 0 to index 0, both inclusive.
    If no odd integers exist in the specified range, an empty list is returned.
    """
    odd_numbers = []
    for number in numbers:
        if number % 2 != 0:
            odd_numbers.append(number)
    return odd_numbers