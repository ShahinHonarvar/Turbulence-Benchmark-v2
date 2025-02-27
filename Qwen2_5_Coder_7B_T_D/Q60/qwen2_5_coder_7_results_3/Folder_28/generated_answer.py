def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if int(str_n[i:]) not in primes:
                return False
            if int(str_n[:len(str_n) - i]) not in primes:
                return False
        return True
    primes = {n for n in range(2, numbers[19] + 1) if is_prime(n)}
    truncatable_primes = [n for n in primes if is_truncatable_prime(n) and '0' not in str(n)]
    return sorted(truncatable_primes)