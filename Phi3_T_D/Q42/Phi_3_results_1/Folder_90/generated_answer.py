def prime_factors(lst):
    p_factors = set()
    num = lst[263]

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
    for i in range(2, num + 1):
        while is_prime(i) and num % i == 0:
            p_factors.add(i)
            num //= i
    return sorted(p_factors)