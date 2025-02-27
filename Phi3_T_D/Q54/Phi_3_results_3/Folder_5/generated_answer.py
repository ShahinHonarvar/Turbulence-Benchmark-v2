def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def right_truncatable_prime(n, primes):
    if not is_prime(n):
        return False
    if n < 10:
        return True
    return is_prime(int(str(n)[:-1])) and n % 10 != 0 and (str(n)[-1] in [str(p) for p in primes]) and right_truncatable_prime(int(str(n)[:-1]), primes)

def all_right_truncatable_prime(numbers):
    if not 0 < len(numbers) <= 56:
        raise ValueError('The argument should be a tuple of positive integers with index 55.')
    if len(numbers) < 56:
        raise ValueError('Tuple does not contain 56 elements.')
    x = numbers[55]
    primes = [str(n) for n in range(2, 10)]
    for n in range(11, x):
        if is_prime(n):
            primes.append(str(n))
    result = [int(start) for start in primes for _ in range(len(start)) if right_truncatable_prime(int(start), [int(p) for p in primes])]
    return sorted(filter(lambda n: n < x, result))