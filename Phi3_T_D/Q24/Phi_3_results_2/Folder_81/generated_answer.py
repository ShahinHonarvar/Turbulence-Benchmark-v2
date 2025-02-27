def sum_of_divisors_in_range(n):
    if n > 3:
        for i in range(3, 5):
            if n % i == 0:
                return n
    return 0