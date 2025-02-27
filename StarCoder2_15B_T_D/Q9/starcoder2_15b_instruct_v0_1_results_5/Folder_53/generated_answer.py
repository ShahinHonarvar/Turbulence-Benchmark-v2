def all_odd_ints_inclusive(numbers):
    """Returns the list of all odd integers from index 100 to index 200, both inclusive."""
    return [number for i, number in enumerate(numbers) if i >= 100 and i <= 200 and (number % 2 == 1)]