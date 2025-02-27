def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def find_primes(n):
        primes = set()
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                primes.add(i)
        if n > 1:
            primes.add(n)
        return primes
    if len(numbers) > 77:
        return find_primes(numbers[77])
    else:
        raise IndexError('List not long enough to have integer at index 77.')