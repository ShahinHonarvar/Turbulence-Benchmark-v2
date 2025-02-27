def sum_of_divisors_in_range(number):
    """
    Returns the sum of all positive divisors of the given number that are between 19 and 69, both inclusive.
    If no such divisors exist, returns 0.
    """
    sum_of_divisors = 0
    for i in range(1, number + 1):
        if number % i == 0 and 19 <= i <= 69:
            sum_of_divisors += i
    return sum_of_divisors