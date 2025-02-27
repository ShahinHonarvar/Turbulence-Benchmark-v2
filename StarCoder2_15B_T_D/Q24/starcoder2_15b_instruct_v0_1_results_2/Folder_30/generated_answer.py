def sum_of_divisors_in_range(n):
    sum_of_divisors = 0
    for i in range(1, n + 1):
        if n % i == 0 and 42 <= i <= 77:
            sum_of_divisors += i
    return sum_of_divisors