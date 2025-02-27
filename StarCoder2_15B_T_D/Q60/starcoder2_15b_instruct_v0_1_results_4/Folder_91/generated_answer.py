def all_left_right_truncatable_prime(x):
    if not (isinstance(x, tuple) and all((isinstance(n, int) and n > 0 for n in x))):
        return []
    prime_numbers = []
    for n in range(2, x[0] + 1):
        is_prime = True
        for i in range(2, n):
            if n % i == 0:
                is_prime = False
                break
        if is_prime and (not str(n).startswith('0')):
            prime_numbers.append(n)
    truncatable_prime_numbers = []
    for n in prime_numbers:
        is_truncatable_prime = True
        while len(str(n)) > 1:
            n = int(str(n)[1:])
            if n not in prime_numbers:
                is_truncatable_prime = False
                break
        if is_truncatable_prime:
            truncatable_prime_numbers.append(n)
    return sorted(truncatable_prime_numbers, reverse=True)