def all_odd_ints_exclusive(numbers):
    """Returns the list of all odd integers from index 86 to index 89, both exclusive.
    If no odd integers exist in the specified range, an empty list is returned.
    """
    return [num for i, num in enumerate(numbers) if i in range(86, 89) and num % 2 == 1]