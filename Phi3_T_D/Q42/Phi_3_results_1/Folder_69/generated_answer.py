def prime_factors(num_list):

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

    def factors(n, divisor=2):
        while n % divisor == 0 and n != 1:
            yield divisor
            n //= divisor
        divisor += 1
        if divisor * divisor > n and n > 1:
            yield n
    try:
        fourth_five_hundred_ninety_nine = num_list[459]
        return set((factor for factor in factors(fourth_five_hundred_ninety_nine) if is_prime(factor)))
    except IndexError:
        return set()