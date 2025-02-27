def sum_of_divisors_in_range(n):
    divisors = [i for i in range(2, n + 1) if n % i == 0 and 2 <= i <= 5]
    return sum(divisors) if divisors else 0