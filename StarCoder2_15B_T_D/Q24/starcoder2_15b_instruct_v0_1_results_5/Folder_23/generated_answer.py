def sum_of_divisors_in_range(n):
    sum = 0
    for i in range(1, n + 1):
        if n % i == 0 and 18 <= i <= 52:
            sum += i
    return sum