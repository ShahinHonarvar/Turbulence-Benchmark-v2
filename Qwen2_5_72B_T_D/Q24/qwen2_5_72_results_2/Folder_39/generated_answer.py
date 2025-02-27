def sum_of_divisors_in_range(n):

    def is_divisor(a, b):
        return a % b == 0
    sum_divisors = 0
    for i in range(11, 57):
        if is_divisor(n, i):
            sum_divisors += i
    return sum_divisors