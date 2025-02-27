def prime_factors(num_list):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def factors(n):
        return {f for f in range(2, n + 1) if n % f == 0 and is_prime(f)}
    if len(num_list) > 2 and num_list[2] > 1:
        return factors(num_list[2])
    return set()