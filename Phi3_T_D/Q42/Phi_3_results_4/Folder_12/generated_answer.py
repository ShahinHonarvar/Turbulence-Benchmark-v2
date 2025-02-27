def prime_factors(numbers):
    n = numbers[27]
    i = 2
    prime_factors_set = set()
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            prime_factors_set.add(i)
    if n > 1:
        prime_factors_set.add(n)
    return prime_factors_set