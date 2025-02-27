def sum_of_divisors_in_range(n):
    sum = 0
    for i in range(1, n + 1):
        if n % i == 0 and 60 <= i <= 86:
            sum += i
    return sum