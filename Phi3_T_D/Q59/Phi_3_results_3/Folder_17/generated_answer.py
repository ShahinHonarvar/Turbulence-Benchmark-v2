def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n, prime_numbers):
        if not is_prime(n):
            return False
        while n > 0:
            if n not in prime_numbers:
                return False
            n = n % 10 ** (len(str(n)) - 1)
        return True
    if len(numbers) > 36:
        x = numbers[36]
    elif len(numbers) == 0:
        return []
    else:
        return []
    prime_numbers = [n for n in range(2, x) if is_prime(n)]
    left_truncatable_primes = [n for n in prime_numbers if len(str(n)) > 1 and is_left_truncatable(n, prime_numbers)]
    return sorted(left_truncatable_primes, reverse=True)