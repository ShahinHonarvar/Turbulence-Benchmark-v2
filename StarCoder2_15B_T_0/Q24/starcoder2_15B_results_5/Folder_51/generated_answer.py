def sum_of_divisors_in_range(n):
    sum_of_divisors = 0
    for i in range(2, n + 1):
        if n % i == 0 and 2 <= i <= 7:
            sum_of_divisors += i
    return sum_of_divisors