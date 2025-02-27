def sum_of_divisors_in_range(num):
    """
    Returns the sum of all divisors of `num` that are between 7 and 8, both inclusive.
    If no such divisors exist, returns 0.
    """
    sum = 0
    for i in range(7, 9):
        if num % i == 0:
            sum += i
    return sum