def sum_of_divisors_in_range(n):
    if not isinstance(n, int) or n <= 0:
        return 0
    divisors = [i for i in range(1, n + 1) if n % i == 0 and 224 <= i <= 584]
    return sum(divisors)