def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n, truncatable):
        str_n = str(n)
        for i in range(1, len(str_n)):
            if not (is_prime(int(str_n[i:])) and is_prime(int(str_n[:i]))):
                return False
        truncatable.add(n)
        return True
    x = numbers[55]
    truncatable_primes = set()
    for number in range(11, x + 1, 2):
        if is_truncatable_prime(number, truncatable_primes):
            pass
    return sorted(truncatable_primes, reverse=True)