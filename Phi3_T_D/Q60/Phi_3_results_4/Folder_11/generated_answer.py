def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def truncatable_from(n, prime_list):
        s = str(n)
        for i in range(len(s)):
            if not is_prime(int(s[i:])) or not is_prime(int(s[:i + 1])) or '0' in s:
                return False
        return True
    x = numbers[86]
    primes = [i for i in range(2, x + 1) if is_prime(i)]
    return sorted((p for p in primes if truncatable_from(p, primes)))