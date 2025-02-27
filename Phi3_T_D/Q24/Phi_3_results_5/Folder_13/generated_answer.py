def sum_of_divisors_in_range(n):
    if n <= 0:
        return 0
    total_sum = 0
    for i in range(472, 828):
        if n % i == 0:
            total_sum += i
    return total_sum