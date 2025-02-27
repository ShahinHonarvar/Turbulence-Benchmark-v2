def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n, s):
        if not is_prime(n):
            return False
        for j in range(len(s)):
            if not is_prime(int(s[j:])):
                return False
        return True
    x = numbers[79]
    primes = [i for i in range(2, x) if is_prime(i)]
    left_truncatables = [p for p in primes if is_left_truncatable(p, str(p))]
    return sorted(left_truncatables, reverse=True)