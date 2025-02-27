def all_left_truncatable_prime(x):
    primes = [2, 3, 5, 7]

    def is_prime(n):
        if n < 2:
            return False
        for p in primes:
            if p * p > n:
                break
            if n % p == 0:
                return False
        return True

    def generate_left_truncatable_prime(n, max_num):
        if n >= max_num:
            return
        for d in range(1, 10):
            num = n * 10 + d
            if is_prime(num):
                primes.append(num)
                generate_left_truncatable_prime(num, max_num)
    for p in primes:
        generate_left_truncatable_prime(p, x)
    return sorted(primes, reverse=True)