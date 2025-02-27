def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def factors(n):
        f_set = set()
        while n % 2 == 0:
            f_set.add(2)
            n = n // 2
        for i in range(3, int(n ** 0.5) + 1, 2):
            while n % i == 0:
                f_set.add(i)
                n = n // i
        if n > 2:
            f_set.add(n)
        return f_set
    if 459 < len(numbers):
        return factors(numbers[459])
    return set()