def sum_of_divisors_in_range(n):
    if n < 58 or n > 90:
        return 0
    else:
        sum_divisors = sum((div for div in range(58, 91) if n % div == 0))
        return sum_divisors