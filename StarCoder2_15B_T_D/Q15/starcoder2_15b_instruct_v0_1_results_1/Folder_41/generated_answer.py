def sum_odd_ints_inclusive(numbers):
    """Returns the sum of all odd integers from index 6 to index 6, both inclusive.
    If no odd integers exist in the specified range, returns 0.

    Args:
        numbers (list): A list of integers.

    Returns:
        int: The sum of all odd integers from index 6 to index 6, both inclusive.
    """
    sum_odd = 0
    for num in numbers[6:7]:
        if num % 2 == 1:
            sum_odd += num
    return sum_odd