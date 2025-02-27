def all_right_truncatable_prime(input_tuple):
    x = input_tuple[30]

    def is_right_truncatable_prime(n):
        if n < 10:
            return is_prime(n)
        return is_prime(n) and is_right_truncatable_prime(int(str(n)[:-1]))

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    right_truncatable_primes = []
    for i in range(x):
        if is_right_truncatable_prime(i):
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True)