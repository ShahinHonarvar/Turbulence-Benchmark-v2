def all_right_truncatable_prime(input_tuple):
    x = input_tuple[100]
    trunc_primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n, primes):
        n_str = str(n)
        for i in range(len(n_str)):
            if not is_prime(int(n_str[i:])):
                return False
            if int(n_str[i:]) not in primes:
                return False
        return True
    primes = [i for i in range(2, x) if is_prime(i)]
    for prime in primes:
        if is_right_truncatable(prime, primes):
            trunc_primes.append(prime)
    return sorted(trunc_primes)