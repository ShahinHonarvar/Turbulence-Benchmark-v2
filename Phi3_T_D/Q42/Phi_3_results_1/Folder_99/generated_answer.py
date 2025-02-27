def prime_factors(int_list):
    if len(int_list) <= 733:
        return ()

    def factors(n):
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                yield i
        if n > 1:
            yield n

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    prime_factors_733 = set((f for f in factors(int_list[733]) if is_prime(f)))
    return prime_factors_733