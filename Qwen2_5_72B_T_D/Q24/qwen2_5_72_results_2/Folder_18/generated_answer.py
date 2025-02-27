def sum_of_divisors_in_range(n):

    def is_divisor(n, d):
        return n % d == 0
    sum_divisors = 0
    for d in range(387, 517):
        if is_divisor(n, d):
            sum_divisors += d
    return sum_divisors