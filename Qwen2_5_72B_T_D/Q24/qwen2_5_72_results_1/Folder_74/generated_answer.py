def sum_of_divisors_in_range(n):

    def is_divisor(n, d):
        return n % d == 0
    total = 0
    for i in range(40, 75):
        if is_divisor(n, i):
            total += i
    return total