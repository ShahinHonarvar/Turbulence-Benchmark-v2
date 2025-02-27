def all_left_right_truncatable_prime(numbers):
    x = numbers[69]

    def is_truncatable_prime(n):
        if n < 2 or (n > 2 and n % 2 == 0) or '0' in str(n):
            return False
        while n > 10:
            n = int(str(n)[1:])
            if n < 2 or (n > 2 and n % 2 == 0) or '0' in str(n):
                return False
        return True
    truncatable_primes = []
    for i in range(1, x + 1):
        if is_truncatable_prime(i):
            truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)