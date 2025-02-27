def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[89]
    primes = [2, 3, 5, 7]
    result = []
    for prime in primes:
        if prime < x:
            result.append(prime)
    for i in range(1, 10):
        for prime in primes[:]:
            new_prime = prime * 10 + i
            if is_prime(new_prime) and new_prime < x:
                primes.append(new_prime)
                result.append(new_prime)
    return sorted(result, reverse=True)