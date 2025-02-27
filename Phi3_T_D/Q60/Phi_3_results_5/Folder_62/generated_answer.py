def all_left_right_truncatable_prime(numbers):

    def is_left_right_truncatable(number, primes):
        s = str(number)
        if len(s) == 1:
            return int(s) in primes
        if int(s) in primes and is_prime(int(s[1:])) and is_left_right_truncatable(int(s[1:]), primes):
            return True
        if int(s[:-1]) in primes and is_prime(int(s[:-1])) and is_left_right_truncatable(int(s[:-1]), primes):
            return True
        return False

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    limit = numbers[70]
    primes = {2, 3, 5, 7}
    truncatable_primes = {p for p in range(2, limit + 1) if is_left_right_truncatable(p, primes)}
    return sorted(list(truncatable_primes))