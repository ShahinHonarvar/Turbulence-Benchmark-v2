def prime_factors(lst):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    if len(lst) < 703:
        return set()

    def factors(n):
        return {i for i in range(2, n + 1) if n % i == 0}
    candidate_factors = factors(lst[702])
    return {p for p in candidate_factors if is_prime(p)}