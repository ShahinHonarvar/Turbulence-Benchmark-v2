def all_left_right_truncatable_prime(nums):
    x = nums[88]
    primes = [True] * (x + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(x ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, x + 1, i):
                primes[j] = False
    truncatable_primes = [i for i in range(2, x + 1) if primes[i] and '0' not in str(i)]

    def is_truncatable(n):
        if n < 10:
            return primes[n]
        return primes[n] and is_truncatable(int(str(n)[1:])) and is_truncatable(int(str(n)[:-1]))
    return sorted([n for n in truncatable_primes if is_truncatable(n)])