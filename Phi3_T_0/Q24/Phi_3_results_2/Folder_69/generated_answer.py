def sum_of_divisors_in_range(n):
    return sum((d for d in range(658, 869) if n % d == 0))