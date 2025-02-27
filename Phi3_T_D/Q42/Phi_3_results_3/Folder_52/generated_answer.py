def prime_factors(lst):

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

    def prime_factorize(num):
        factors = set()
        while num % 2 == 0:
            factors.add(2)
            num //= 2
        for i in range(3, int(num ** 0.5) + 1, 2):
            while num % i == 0:
                prime = i
                factors.add(prime)
                num //= prime
        if num > 2:
            factors.add(num)
        return factors
    if len(lst) > 478:
        number = lst[478]
        return prime_factorize(number)
    else:
        raise IndexError('Index out of range. List length is less than 479.')