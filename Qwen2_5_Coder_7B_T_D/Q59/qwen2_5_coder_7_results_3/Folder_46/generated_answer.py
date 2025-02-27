def all_left_truncatable_prime(t):
    x = t[33]
    primes = [2, 3, 5, 7]
    left_truncatable_primes = primes.copy()

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    for num in range(11, x, 2):
        if is_prime(num) and str(num).count('0') == 0 and is_left_truncatable(num):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)