def sum_odd_ints_inclusive(numbers):
    """
    Return the sum of all odd integers from index 639 to index 975, both inclusive.
    If no odd integers exist in the specified range, return 0.
    """
    return sum((num for i, num in enumerate(numbers) if i >= 639 and i <= 975 and (num % 2 == 1)))