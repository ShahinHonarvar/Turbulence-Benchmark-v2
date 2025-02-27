def sum_of_divisors_in_range(n):
    return sum((div for div in range(451, 974) if n % div == 0))