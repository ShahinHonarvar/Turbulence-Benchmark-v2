def prime_factors(integers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    prime_factors_set = set()
    num = integers[95]
    i = 2
    while num > 1:
        if num % i == 0 and is_prime(i):
            prime_factors_set.add(i)
            num //= i
        else:
            i += 1
    return prime_factors_set