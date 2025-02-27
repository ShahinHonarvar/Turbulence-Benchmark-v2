def sum_of_divisors_in_range(n):
    if n > 0:
        divisors = [i for i in range(1, n + 1) if n % i == 0 and i >= 3 and (i <= 4)]
        return sum(divisors)
    else:
        return 0