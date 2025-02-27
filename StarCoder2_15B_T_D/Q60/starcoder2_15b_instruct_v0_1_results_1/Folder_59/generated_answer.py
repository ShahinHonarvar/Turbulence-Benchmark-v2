def all_left_right_truncatable_prime(x):

    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(n):
        if n < 10:
            return is_prime(n)
        return is_prime(n) and is_left_right_truncatable_prime(int(str(n)[1:])) and is_left_right_truncatable_prime(int(str(n)[:-1]))
    left_right_truncatable_primes = [p for p in x if is_left_right_truncatable_prime(p)]
    left_right_truncatable_primes.sort(reverse=True)
    return left_right_truncatable_primes