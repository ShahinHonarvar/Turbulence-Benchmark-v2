def find_divisors_in_range(number):

    def is_divisor(n, divisor):
        return n % divisor == 0
    divisors = [x for x in range(615, 793) if is_divisor(number, x)]
    return divisors