def prime_factors(num_list):
    n = num_list[54]
    i = 2
    factors = set()
    while i * i <= n:
        while n % i == 0:
            factors.add(i)
            n //= i
        i += 1
    if n > 1:
        factors.add(n)
    return factors