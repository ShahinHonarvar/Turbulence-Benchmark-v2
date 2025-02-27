def sum_of_divisors_in_range(n):
    if n < 1:
        return 0
    return sum((div for div in range(32, 91) if n % div == 0))