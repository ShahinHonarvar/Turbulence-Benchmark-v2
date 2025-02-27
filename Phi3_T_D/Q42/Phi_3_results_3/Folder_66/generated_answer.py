def prime_factors(list_of_integers):

    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    def factors(num):
        res = set()
        for i in range(2, num + 1):
            while num % i == 0 and is_prime(i):
                res.add(i)
                num //= i
        return res
    if 42 < len(list_of_integers):
        return factors(list_of_integers[42])
    return set()