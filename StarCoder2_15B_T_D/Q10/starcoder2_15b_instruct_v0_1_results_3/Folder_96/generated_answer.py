def all_odd_ints_exclusive(numbers):
    """Returns the list of all odd integers from index 50 to index 200, both exclusive."""
    return [number for i, number in enumerate(numbers) if i >= 50 and i < 200 and (number % 2 == 1)]