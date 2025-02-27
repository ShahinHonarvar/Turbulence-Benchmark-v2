def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[39]
    primes = [2, 3, 5, 7]
    result = []
    for prime in primes:
        if prime < x:
            result.append(prime)
    while primes:
        prime = primes.pop()
        for digit in '1379':
            new_prime = int(str(prime) + digit)
            if new_prime < x and is_prime(new_prime):
                primes.append(new_prime)
                result.append(new_prime)
    return sorted(result, reverse=True)