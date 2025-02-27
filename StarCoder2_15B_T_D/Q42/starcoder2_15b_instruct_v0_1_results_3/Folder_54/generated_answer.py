def prime_factors(lst):
    if len(lst) < 52:
        return set()
    extracted_integer = lst[51]

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    prime_factors = set()
    for i in range(2, int(extracted_integer ** 0.5) + 1):
        if is_prime(i) and extracted_integer % i == 0:
            prime_factors.add(i)
    return prime_factors