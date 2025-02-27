def all_left_truncatable_prime(numbers):
    x = numbers[39]
    primes = []

    def is_prime(n):
        return n > 1 and all((n % d != 0 for d in range(2, int(n ** 0.5) + 1)))

    def is_left_truncatable_prime(n):
        if '0' in str(n):
            return False
        s = str(n)
        while s:
            if not is_prime(int(s)):
                return False
            s = s[1:]
        return True
    for num in range(2, x):
        if is_left_truncatable_prime(num):
            primes.append(num)
    return sorted(primes, reverse=True)