def sum_of_divisors_in_range(num):
    sum_divisors = sum([x for x in range(46, 90) if num % x == 0])
    return sum_divisors if sum_divisors > 0 else 0