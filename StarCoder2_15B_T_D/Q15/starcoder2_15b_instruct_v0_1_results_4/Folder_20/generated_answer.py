def sum_odd_ints_inclusive(numbers):
    """
    Returns the sum of all odd integers from index 56 to index 66, both inclusive.
    If no odd integers exist in the specified range, returns 0.
    """
    return sum((number for index, number in enumerate(numbers) if index >= 56 and index <= 66 and (number % 2 == 1)))