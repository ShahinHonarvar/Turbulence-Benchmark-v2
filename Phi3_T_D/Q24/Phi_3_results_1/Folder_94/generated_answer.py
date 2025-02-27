def sum_of_divisors_in_range(n):

    def valid_divisor(divisor):
        return 35 <= divisor <= 37
    return sum((divisor for divisor in range(1, n + 1) if n % divisor == 0 and valid_divisor(divisor)))