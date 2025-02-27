def all_odd_ints_inclusive(numbers):
    """Returns the list of all odd integers from index 80 to index 200, both inclusive."""
    return [number for number in numbers[80:201] if number % 2 != 0]