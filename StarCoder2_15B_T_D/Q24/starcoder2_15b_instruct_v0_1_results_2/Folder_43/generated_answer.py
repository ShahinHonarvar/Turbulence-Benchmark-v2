def sum_of_divisors_in_range(n):
    sum_of_divisors = 0
    for i in range(1, n + 1):
        if n % i == 0:
            if 19 <= i <= 69:
                sum_of_divisors += i
    if 19 <= sum_of_divisors <= 69:
        return sum_of_divisors
    else:
        return 0