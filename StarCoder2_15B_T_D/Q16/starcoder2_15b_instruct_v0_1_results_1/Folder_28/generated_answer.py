def sum_even_ints_inclusive(numbers):
    """
    Returns the sum of all even integers from index 62 to index 63, both inclusive.
    If no even integers exist in the specified range, returns 0.
    """
    if not isinstance(numbers, list) or not all((isinstance(n, int) for n in numbers)):
        raise TypeError('The argument must be a list of integers.')
    even_ints = [n for n in numbers[62:64] if n % 2 == 0]
    return sum(even_ints) if even_ints else 0