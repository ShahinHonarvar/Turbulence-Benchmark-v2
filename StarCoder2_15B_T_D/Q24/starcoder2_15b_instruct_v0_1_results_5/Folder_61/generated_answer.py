def sum_of_divisors_in_range(num):
    """
    This function takes a positive integer as its argument, and returns the sum of all
    positive divisors of the given integer that are between 2 and 3, both inclusive.
    If no such divisors exist in the specified range, the function returns 0.
    """
    sum_of_divisors = 0
    for i in range(1, num + 1):
        if num % i == 0 and 2 <= i <= 3:
            sum_of_divisors += i
    return sum_of_divisors