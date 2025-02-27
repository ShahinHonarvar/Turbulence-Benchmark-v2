def sum_of_divisors_in_range(n):

    def is_divisor(x):
        return n % x == 0
    return sum((x for x in range(3, 6) if is_divisor(x)))