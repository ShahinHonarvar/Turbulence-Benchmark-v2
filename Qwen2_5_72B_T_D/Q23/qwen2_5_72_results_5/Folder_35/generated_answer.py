def find_divisors_in_range(n):

    def is_divisor(x):
        return n % x == 0
    return [x for x in range(392, 466) if is_divisor(x)]