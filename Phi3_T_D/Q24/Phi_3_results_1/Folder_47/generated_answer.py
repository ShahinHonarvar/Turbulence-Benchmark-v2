def sum_of_divisors_in_range(n):
    result = 0
    for i in range(27, 45):
        if 0 < n % i < 1:
            result += i
    return result