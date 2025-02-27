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
            if '0' in s or not is_prime(int(s[i:])):
                return False
        return True
    x = numbers[11]
    left_truncatable_primes = [n for n in range(2, x) if is_left_truncatable(n)]
    return left_truncatable_primes