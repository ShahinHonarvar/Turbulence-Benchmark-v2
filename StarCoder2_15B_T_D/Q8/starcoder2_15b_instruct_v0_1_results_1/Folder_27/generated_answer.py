def all_even_ints_exclusive(numbers):
    """Returns the list of all even integers from index 28 to index 49, both exclusive.
    If no even integers exist in the specified range, returns an empty list.
    """
    if len(numbers) < 49:
        return []
    return [num for num in numbers[28:49] if num % 2 == 0]