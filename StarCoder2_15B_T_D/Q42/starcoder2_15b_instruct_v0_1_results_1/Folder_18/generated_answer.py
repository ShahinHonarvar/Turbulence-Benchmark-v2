def prime_factors(lst):
    n = lst[312]
    if n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                prime_factors = {i}
                while n % i == 0:
                    n //= i
                if n > 1:
                    prime_factors |= prime_factors(lst)
                return prime_factors
    return {n}