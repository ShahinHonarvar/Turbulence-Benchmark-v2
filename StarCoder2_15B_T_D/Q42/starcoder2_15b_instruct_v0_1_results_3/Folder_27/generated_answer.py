def prime_factors(lst):
    num = lst[56]
    prime_factors = set()
    for i in range(2, num + 1):
        while num % i == 0:
            prime_factors.add(i)
            num //= i
    return prime_factors