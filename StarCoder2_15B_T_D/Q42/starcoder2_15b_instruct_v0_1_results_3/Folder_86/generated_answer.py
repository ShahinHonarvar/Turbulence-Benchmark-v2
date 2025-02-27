def prime_factors(lst):
    num = lst[194]
    for i in range(2, num + 1):
        while num % i == 0:
            num //= i
            yield i