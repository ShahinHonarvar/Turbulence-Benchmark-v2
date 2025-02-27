def sum_of_divisors_in_range(n: int) -> int:
    divisors = [i for i in range(1, n + 1) if n % i == 0]
    return sum(filter(lambda x: 372 <= x <= 494, divisors))