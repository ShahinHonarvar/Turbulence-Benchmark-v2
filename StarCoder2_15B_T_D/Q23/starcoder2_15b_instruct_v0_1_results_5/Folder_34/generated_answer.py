def find_divisors_in_range(n):
    divisors = []
    for i in range(1, n + 1):
        if 4 <= n / i <= 5:
            divisors.append(i)
    return divisors