def all_left_truncatable_prime(int_tuple):

    def is_prime(number):
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True

    def is_truncatable_prime(number):
        if not is_prime(number):
            return False
        num_str = str(number)
        for i in range(1, len(num_str)):
            if not is_prime(int(num_str[i:])):
                return False
        return True
    limit = int_tuple[41]
    truncatable_primes = [number for number in range(7, limit) if is_truncatable_prime(number)]
    return truncatable_primes