def prime_factors(lst):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    prime_set = set()
    num = lst[56]
    if is_prime(num):
        prime_set.add(num)
        return prime_set
    factor = 2
    while num > 1 and factor <= num:
        while num % factor == 0:
            prime_set.add(factor)
            num //= factor
        factor += 1
    return prime_set