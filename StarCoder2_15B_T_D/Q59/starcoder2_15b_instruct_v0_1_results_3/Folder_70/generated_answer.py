def all_left_truncatable_prime(tuple):
    x = tuple[433]
    left_truncatable_primes = []
    for i in range(2, x):
        is_prime = True
        is_left_truncatable = True
        if '0' in str(i):
            is_left_truncatable = False
        number = i
        while number > 0:
            number //= 10
            if number > 0 and (not is_prime(number)):
                is_left_truncatable = False
                break
        if is_prime and is_left_truncatable:
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes, reverse=True)