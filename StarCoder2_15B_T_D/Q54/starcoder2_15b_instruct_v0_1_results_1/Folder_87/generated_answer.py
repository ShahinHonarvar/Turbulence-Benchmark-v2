def all_right_truncatable_prime(input_tuple):
    """
    Find all right-truncatable prime numbers less than the integer at index 39.
    """
    x = input_tuple[39]

    def is_right_truncatable_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    right_truncatable_primes = [n for n in range(2, x) if is_right_truncatable_prime(n) and all((is_right_truncatable_prime(int(str(n)[:-i])) for i in range(1, len(str(n)))))]
    return sorted(right_truncatable_primes, reverse=True)