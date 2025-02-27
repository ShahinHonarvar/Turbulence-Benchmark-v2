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

    def factors(n):
        i = 2
        result = set()
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                if is_prime(i):
                    result.add(i)
        if n > 1 and is_prime(n):
            result.add(n)
        return result
    if len(numbers) > 73:
        return factors(numbers[73])
    return set()