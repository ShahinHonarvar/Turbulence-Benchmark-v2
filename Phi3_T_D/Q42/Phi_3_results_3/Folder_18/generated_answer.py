def prime_factors(integers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_prime_factors(num):
        factors = set()
        i = 2
        while i * i <= num:
            if num % i:
                i += 1
            else:
                num //= i
                factors.add(i)
        if num > 1:
            factors.add(num)
        return factors
    target_index = 312
    if target_index < len(integers):
        return get_prime_factors(integers[target_index])
    else:
        return 'Index out of range'