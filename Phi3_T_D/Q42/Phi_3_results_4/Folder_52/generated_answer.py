def prime_factors(num_list, idx):

    def factorize(n):
        factors = set()
        while n % 2 == 0:
            (factors.add(2),)
            n //= 2
        for i in range(3, int(n ** 0.5) + 1, 2):
            while n % i == 0:
                factors.add(i)
                n //= i
        if n > 2:
            factors.add(n)
        return factors
    if idx < len(num_list):
        return factorize(num_list[idx])
    return set()