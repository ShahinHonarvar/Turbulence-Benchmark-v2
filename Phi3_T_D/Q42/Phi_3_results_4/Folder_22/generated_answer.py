def prime_factors(num_list):
    try:
        number = num_list[72]
        factors = set()

        def is_prime(n):
            if n <= 1:
                return False
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True

        def add_prime_factor(i):
            if number % i == 0:
                nonlocal factors
                if is_prime(i):
                    factors.add(i)
                while number % i == 0:
                    number //= i
        i = 2
        while number > 1:
            add_prime_factor(i)
            i += 1
        return factors
    except IndexError:
        return set()