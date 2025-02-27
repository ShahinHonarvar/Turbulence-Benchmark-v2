def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def factors(n, i=2):
        results = []
        while i <= n:
            if n % i == 0 and is_prime(i):
                results.append(i)
            i += 1
        return results
    n = numbers[790]
    return set(factors(n))