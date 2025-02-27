def prime_factors(lst):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_factor(n, factor=2):
        while not n % factor:
            if is_prime(factor):
                yield factor
            n //= factor
    if len(lst) > 66:
        nonlocal_index = 66
        numbers = lst[nonlocal_index]
        return set(get_factor(numbers))
    else:
        raise IndexError('The list is too short.')