def all_left_right_truncatable_prime(x):
    """
    Returns a list of all left- and right-truncatable prime numbers less than or equal to x.
    """

    def is_truncatable_prime(num):
        if num in [2, 3, 5, 7]:
            return True
        if num < 10 or num % 10 == 0 or num % 2 == 0:
            return False
        digits = [int(d) for d in str(num)]
        for i in range(len(digits) - 1):
            left = int(''.join((str(d) for d in digits[i:])))
            right = int(''.join((str(d) for d in digits[:i + 1])))
            if left % 2 == 0 or right % 2 == 0:
                return False
        return True

    def generate_truncatable_primes(x):
        truncatable_primes = []
        for num in range(2, x + 1):
            if is_truncatable_prime(num):
                truncatable_primes.append(num)
        return truncatable_primes
    return sorted(generate_truncatable_primes(x), reverse=True)