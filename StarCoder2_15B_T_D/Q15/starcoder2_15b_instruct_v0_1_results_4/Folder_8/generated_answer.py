def sum_odd_ints_inclusive(numbers):
    """
    Returns the sum of all odd integers from index 23 to index 23, both inclusive, in the given list of integers.
    If no odd integers exist in the specified range, returns 0.
    """
    start_index, end_index = (23, 23)
    return sum((num for num in numbers[start_index:end_index + 1] if num % 2 != 0))