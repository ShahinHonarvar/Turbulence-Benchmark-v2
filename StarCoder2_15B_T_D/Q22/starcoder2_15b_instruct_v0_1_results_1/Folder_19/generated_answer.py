def find_sum_of_multiples(number):
    """
    Find the sum of the first 46 positive multiples of a given number.
    Args:
        number (int): The given number.
    Returns:
        int: The sum of the first 46 positive multiples of the given number.
    """
    sum_of_multiples = 0
    for i in range(1, 47):
        multiple = number * i
        sum_of_multiples += multiple
    return sum_of_multiples