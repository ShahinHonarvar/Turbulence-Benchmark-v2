def all_right_truncatable_prime(input_tuple):
    """
    Returns a sorted list of all right-truncatable prime numbers less than the integer at index 100.
    """
    x = input_tuple[100]

    def is_truncatable_prime(num):
        if num < 2:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                return False
        return True
    right_truncatable_primes = [p for p in range(2, x) if is_truncatable_prime(p)]
    return sorted(right_truncatable_primes, reverse=True)