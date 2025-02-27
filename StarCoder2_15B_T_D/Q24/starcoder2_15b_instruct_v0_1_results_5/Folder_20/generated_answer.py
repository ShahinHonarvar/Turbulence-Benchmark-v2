def sum_of_divisors_in_range(n):
    divisors = [i for i in range(1, n + 1) if n % i == 0]
    divisors_in_range = [d for d in divisors if 28 <= d <= 81]
    if len(divisors_in_range) == 0:
        return 0
    else:
        return sum(divisors_in_range)