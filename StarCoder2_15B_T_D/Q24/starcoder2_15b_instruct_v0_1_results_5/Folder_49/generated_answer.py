def sum_of_divisors_in_range(n):
    sum = 0
    for i in range(2, n + 1):
        if n % i == 0 and 2 <= i <= 6:
            sum += i
    return sum