def sum_of_divisors_in_range(n):
    return sum((div for div in range(59, 89) if n % div == 0))