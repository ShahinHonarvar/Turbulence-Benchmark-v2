def is_left_right_truncatable(n, primes):
    str_n = str(n)
    for i in range(len(str_n)):
        if int(str_n[i:]) not in primes:
            return False
        if i > 0 and str_n[:len(str_n) - i] not in primes:
            return False
    return True

def all_left_right_truncatable_prime(numbers_tuple):
    if len(numbers_tuple) < 88:
        raise ValueError('Tuple must contain at least 88 integer elements.')
    x = numbers_tuple[88]
    truncatable_primes = []
    primes = set()
    num_range = (2, x + 1)
    for possible_prime in range(*num_range):
        if possible_prime not in primes:
            is_prime = all((possible_prime % num != 0 for num in range(2, int(possible_prime ** 0.5) + 1)))
            if is_prime:
                primes.add(possible_prime)
                if is_left_right_truncatable(possible_prime, primes):
                    truncatable_primes.append(possible_prime)
    return sorted(truncatable_primes, reverse=True)