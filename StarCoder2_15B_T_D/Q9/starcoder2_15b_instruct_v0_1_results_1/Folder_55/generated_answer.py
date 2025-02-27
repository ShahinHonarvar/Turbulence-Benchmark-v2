def all_odd_ints_inclusive(numbers):
    """
    Return a list of all odd integers from index 10 to index 10, both inclusive.
    If no odd integers exist in the specified range, return an empty list.
    """
    return [num for i, num in enumerate(numbers) if i >= 10 and i <= 10 and (num % 2 == 1)]