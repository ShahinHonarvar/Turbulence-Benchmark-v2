def prime_factors(int_list):
    num_to_factors = {}

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for num in int_list:
        factors = []
        for i in range(2, num + 1):
            while num % i == 0 and is_prime(i):
                factors.append(i)
                num //= i
        num_to_factors[num] = factors
    return num_to_factors.get(int_list[96], [])