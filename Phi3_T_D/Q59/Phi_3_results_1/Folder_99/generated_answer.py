def all_left_truncatable_prime(nums):

    def is_prime(n, sieve):
        return n in sieve

    def generate_sieve(limit):
        sieve = [True] * limit
        sieve[0] = sieve[1] = False
        for i in range(2, int(limit ** 0.5) + 1):
            if sieve[i]:
                for j in range(i * i, limit, i):
                    sieve[j] = False
        return sieve

    def is_left_truncatable_prime(n, sieve):
        str_n = str(n)
        while str_n:
            if not is_prime(int(str_n), sieve):
                return False
            str_n = str_n[1:]
        return True
    x = nums[758]
    prime_sieve = generate_sieve(x + 1)
    truncatable_primes = [i for i in range(2, x) if is_left_truncatable_prime(i, prime_sieve)]
    return truncatable_primes