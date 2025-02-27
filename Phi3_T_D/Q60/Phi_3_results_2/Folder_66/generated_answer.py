def all_left_right_truncatable_prime(num_tuple):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_truncatable(prime):
        str_prime = str(prime)
        for i in range(1, len(str_prime)):
            if not is_prime(int(str_prime[i:])) or not is_prime(int(str_prime[:-i])):
                return False
        return True
    x = num_tuple[25]
    primes = [i for i in range(2, x + 1) if is_prime(i)]
    truncatable_primes = [p for p in primes if is_truncatable(p)]
    return sorted(truncatable_primes, reverse=True)