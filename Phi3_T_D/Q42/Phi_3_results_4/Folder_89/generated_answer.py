def prime_factors(nums):

    def factors(n):
        primes = []
        d = 2
        while d * d <= n:
            while n % d == 0:
                primes.append(d)
                n //= d
            d += 1
        if n > 1:
            primes.append(n)
        return primes
    try:
        return set(factors(nums[18]))
    except IndexError:
        return 'Index out of range'