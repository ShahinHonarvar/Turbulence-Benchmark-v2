def find_divisors_in_range(number):

    def is_divisor(divisor):
        return number % divisor == 0
    return [d for d in range(4, 8) if is_divisor(d)]