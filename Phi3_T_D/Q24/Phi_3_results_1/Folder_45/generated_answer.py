def sum_of_divisors_in_range(num):
    return sum((div for div in range(4, 9) if num % div == 0))