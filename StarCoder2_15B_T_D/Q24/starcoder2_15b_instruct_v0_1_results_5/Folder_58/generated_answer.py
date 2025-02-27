def sum_of_divisors_in_range(num):
    """
    Returns the sum of all positive divisors of `num` that are between 403 and 514, both inclusive.
    If no such divisors exist in the specified range, returns 0.
    """
    sum_of_divisors = 0
    for i in range(403, 515):
        if num % i == 0:
            sum_of_divisors += i
    return sum_of_divisors