def sum_of_divisors_in_range(n):

    def is_divisor(number):
        return n % number == 0 and 111 <= number <= 508
    return sum((number for number in range(1, n + 1) if is_divisor(number)))