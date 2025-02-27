def sum_of_divisors_in_range(n):

    def is_divisor(x, n):
        return n % x == 0
    sum_divisors = 0
    for i in range(461, 828):
        if is_divisor(i, n):
            sum_divisors += i
    return sum_divisors