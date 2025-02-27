def is_prime(n):
    if n <= 1:
        return False
    if n % 2 == 0 and n > 2:
        return False
    sqrt_n = int(n ** 0.5)
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(int_tuple):
    x = int_tuple[93]
    truncable_primes = []

    def is_left_truncatable(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if not is_prime(int(str_n[i:])):
                return False
        return True
    for number in range(2, x):
        if is_left_truncatable(number):
            truncable_primes.append(number)
    return truncable_primes