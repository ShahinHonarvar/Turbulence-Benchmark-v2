def prime_factors(integers):
    prime_factors_set = set()
    n = integers[38]
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            prime_factors_set.add(divisor)
            n //= divisor
        divisor += 1
        if divisor * divisor > n:
            if n > 1:
                prime_factors_set.add(n)
            break
    return prime_factors_set