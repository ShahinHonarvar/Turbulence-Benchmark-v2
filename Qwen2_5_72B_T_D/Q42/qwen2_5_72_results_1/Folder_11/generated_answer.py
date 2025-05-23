def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def find_prime_factors(n):
        prime_factors = set()
        for i in range(2, n + 1):
            if n % i == 0 and is_prime(i):
                prime_factors.add(i)
        return prime_factors
    if len(numbers) < 78:
        return set()
    else:
        return find_prime_factors(numbers[77])