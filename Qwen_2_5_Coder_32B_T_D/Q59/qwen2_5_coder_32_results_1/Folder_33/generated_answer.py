def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        s = str(n)
        for i in range(len(s)):
            if not is_prime(int(s[i:])) or '0' in s:
                return False
        return True
    x = numbers[945]
    left_truncatable_primes = [n for n in range(2, x) if is_left_truncatable(n)]
    return sorted(left_truncatable_primes, reverse=True)