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
        result = set()
        d = 2
        while d * d <= n:
            if n % d == 0:
                result.add(d)
                n //= d
            else:
                d += 1
        if n > 1:
            result.add(n)
        return result
    if len(numbers) < 248:
        return set()
    num = numbers[247]
    return factors(num)