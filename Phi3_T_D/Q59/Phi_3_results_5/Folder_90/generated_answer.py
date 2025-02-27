def is_left_truncatable_prime(n, prime_checker, primes):
    if n not in primes:
        return False
    n_str = str(n)
    for i in range(len(n_str)):
        if not prime_checker(int(n_str[i:])):
            return False
    return True

def all_left_truncatable_prime(tup):
    primes = [2, 3, 5, 7]
    numbers = range(2, tup[465], 2)[3:]
    for prime in [23, 37, 53, 73, 313, 317, 373, 797, 3137, 3797, 739397]:
        primes.append(prime)
    prime_checker = lambda num: num in primes or not [x for x in primes if x % num != 0]
    left_truncatable_primes = [num for num in numbers if is_left_truncatable_prime(num, prime_checker, primes)]
    return left_truncatable_primes