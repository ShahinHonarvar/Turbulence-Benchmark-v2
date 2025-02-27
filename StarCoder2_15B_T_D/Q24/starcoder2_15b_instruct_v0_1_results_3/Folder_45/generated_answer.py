def sum_of_divisors_in_range(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    filtered_divisors = [d for d in divisors if 4 <= d <= 8]
    return sum(filtered_divisors) if filtered_divisors else 0