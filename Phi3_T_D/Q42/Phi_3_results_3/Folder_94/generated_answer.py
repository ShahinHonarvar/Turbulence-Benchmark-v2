def prime_factors(ints):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    factor_set = set()
    if 93 < len(ints):
        num = ints[93]
        for i in range(2, num + 1):
            if num % i == 0 and is_prime(i):
                factor_set.add(i)
    else:
        return "Error: The list doesn't contain an item at index 93"
    return factor_set