def sum_of_divisors_in_range(num: int) -> int:
    """
    Returns the sum of all divisors of `num` that are between 2 and 5, inclusive.
    If no such divisors exist, returns 0.
    """
    divisors = []
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            divisors.append(i)
            if i != num // i:
                divisors.append(num // i)
    return sum((d for d in divisors if 2 <= d <= 5))